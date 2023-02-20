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
        self.weights = numpy.random.rand(rSC.numSensorNeurons, rSC.numMotorNeurons)
        self.weights = self.weights * 2 - 1

        print(rSC.numSensorNeurons)
        print(rSC.numMotorNeurons)
        

        self.myID = nextAvailableID
        print("My ID: " + str(self.myID) + " My weights:")
        print(self.weights)
        print(self.weights[rSC.numSensorNeurons-1][rSC.numMotorNeurons-1])

    
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

    def Make_Snake(self):
        self.snake = {}

        for linkName in range(rSC.numLinks):
            pass

    def Create_Snake(self):
        self.body = {}
        pyrosim.Start_URDF("body.urdf")

        for linkName in range(rSC.numLinks):
            if linkName == 0:
                prevFace = 0
                self.body[linkName] = SnakeBody(linkName,prevFace,0)

            else:
                prevFace = self.body[linkName-1].faceNum
                prevDimensions = self.body[linkName-1].dimensions
                self.body[linkName] = SnakeBody(linkName,prevFace,prevDimensions)

        pyrosim.End()
        print(self.body)
        return()


    def Create_Snake_Brain(self):
        self.neuronNum = 0
        self.sensorNum = 0
        self.motorNum = 0
        print(rSC.numLinks)

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
            
        for currentRow in range(rSC.numSensorNeurons):
            for currentColumn in range(rSC.numMotorNeurons-1):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+self.sensorNum), weight = self.weights[currentRow][currentColumn])
        
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

    def Mutate_Brain(self):
        pass

    def Mutate_Body(self):
        pass

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

