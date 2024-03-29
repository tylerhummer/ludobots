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
        self.weights = numpy.random.rand(rSC.numSensorNeurons,rSC.numLinks)   #*** Use this line for random seed 5 and 124 and 444 and 7760 and 1121***
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        print("My ID: " + str(self.myID))
        self.mutation_selection = 0
        self.link_select = 10
        

    
    def Evaluate(self, directOrGUI):
        if self.myID <= 14:
            self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()

        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        while True:
            try:
                fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
                break
            except:
                pass
        while True:
            if float(fitnessFile.read()) == "":
                self.fitness = 0
                break
            else:
                self.fitness = float(fitnessFile.read())
                break
        
        print('fitness = ', self.fitness)
        fitnessFile.close()

    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.End()
        return


    def Create_Snake(self):
        self.body = {}
        link_select = self.link_select
        sensor_tracker = 0
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        for linkName in range(rSC.numLinks):
            sensor_val = random.randint(0,1)
            if ((rSC.numSensorNeurons)-linkName) <= sensor_tracker:
                sensor_val = 1
            if sensor_tracker >= rSC.numSensorNeurons:
                sensor_val = 0
            sensor_tracker += sensor_val

            if linkName == 0:
                prevFace = 0
                self.body[linkName] = SnakeBody(linkName,prevFace,0,sensor_val, self.mutation_selection, link_select)
                link_select -= 1

            else:
                prevFace = self.body[linkName-1].faceNum
                prevDimensions = self.body[linkName-1].dimensions
                self.body[linkName] = SnakeBody(linkName,prevFace,prevDimensions,sensor_val, self.mutation_selection, link_select)
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

        #print(self.sensorNum)
        #print(self.motorNum)
        
        #self.weights = numpy.random.rand(self.sensorNum, self.motorNum)
        #self.weights = self.weights * 2 - 1
        #print(self.weights)
        #print(self.weights.shape)
        self.weights = numpy.random.rand(self.neuronNum,rSC.numLinks)
        self.weights = self.weights * 2 - 1
        for currentRow in range(self.sensorNum):
            for currentColumn in range(self.motorNum):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+self.sensorNum), weight = self.weights[currentRow-1][currentColumn-1])
        
        pyrosim.End()
        return()



    def Start_Simulation(self, directOrGUI):
        #self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()
        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        try: 
            self.fitness = float(fitnessFile.read())
        
        except ValueError:
            self.fitness = 0
        print('fitness = ', self.fitness)
        fitnessFile.close()




    def Mutate(self, currentGeneration):
        #self.weights[0][0] = random.random() * 2 - 1
        if currentGeneration == 0:
            pass
                        
        else:
            #random.seed(None)
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

