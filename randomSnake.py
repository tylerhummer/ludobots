import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import randomSnakeConstants as rSC
from randomSnakeBody import SnakeBody
from randomSnakeBrain import snakeBrain

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(6,9)   #*** Use this line for random seed 5 and 124 and 444 and 7766 and 7760***
        #self.weights = numpy.random.rand(5,9)   #*** Use this line for random seed 77***
        #self.weights = numpy.random.rand(4,9)  #*** Use this line for random seed 111***
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        print("My ID: " + str(self.myID))
        self.mutation_selection = 0
        self.link_select = 10
        

    
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()

        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read())
        print('fitness = ', self.fitness)
        fitnessFile.close()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
        return


    def Create_Snake(self):
        self.body = {}
        seed_number = rSC.seed_number
        link_select = self.link_select
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        for linkName in range(rSC.numLinks):
            if linkName == 0:
                prevFace = 0
                self.body[linkName] = SnakeBody(linkName,prevFace,0,seed_number, self.mutation_selection, link_select)
                seed_number += 1
                link_select -= 1

            else:
                prevFace = self.body[linkName-1].faceNum
                prevDimensions = self.body[linkName-1].dimensions
                self.body[linkName] = SnakeBody(linkName,prevFace,prevDimensions,seed_number, self.mutation_selection, link_select)
                seed_number += 1
                link_select -= 1


        pyrosim.End()
        #print(self.body)
        return()


    def Create_Snake_Brain(self):
        self.neuronNum = 0
        self.sensorNum = 0
        self.motorNum = 0
        #print("number of links ", rSC.numLinks)
        #print(self.weights)
        #print(self.weights.shape)

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        for part in self.body:
            if self.body[part].sense == 1:
                pyrosim.Send_Sensor_Neuron(name = self.neuronNum, linkName = str(self.body[part].linkName))
                self.neuronNum += 1
                self.sensorNum += 1

        for part in self.body:
            if part < rSC.numLinks-1:
                pyrosim.Send_Motor_Neuron(name = self.neuronNum, jointName = str(self.body[part].jointName))
                self.neuronNum += 1
                self.motorNum += 1

        #self.weights = numpy.random.rand(self.sensorNum, self.motorNum)
        #self.weights = self.weights * 2 - 1
        #print(self.weights)
        #print(self.weights.shape)

        for currentRow in range(self.sensorNum):
            for currentColumn in range(self.motorNum):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+self.sensorNum), weight = self.weights[currentRow-1][currentColumn-1])
        
        pyrosim.End()
        return()



    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()
        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read())
        print('fitness = ', self.fitness)
        fitnessFile.close()


    def Mutate(self, currentGeneration):
        #self.weights[0][0] = random.random() * 2 - 1
        if currentGeneration == 0:
            pass
                        
        else:
            random.seed(None)
            pick = random.random()
            if pick >= 0.3:     # 70% chance of sensor-motor neuron mutation
                self.mutation_selection = 1
                self.weights[random.randint(0,self.sensorNum-1)][random.randint(0,self.motorNum-1)] = random.random() * 2 - 1
                self.link_select = 10

            elif pick < 0.1:    # 10% chance of link size mutation
                self.mutation_selection = 3
                self.link_select = random.randint(0,9) #randomize which link will be the one that changes

            else:               # 20% chance of joint orientation mutation
                self.mutation_selection = 2
                self.link_select = random.randint(0,8) #randomize which link will be the one that changes
            
            
        #self.weights[random.randint(0,self.sensorNum-1)][random.randint(0,self.motorNum-1)] = random.random() * 2 - 1
        #self.weights = weights
        #return self.weights


    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

