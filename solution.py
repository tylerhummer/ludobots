import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    
    def __init__ (self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.length = 1
        self.width = 1
        self.height = 1
        self.myID = nextAvailableID
        print("My ID: " + str(self.myID) + " My weights:")
        print(self.weights)

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + str(directOrGUI) + " " + str(self.myID))
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read())
        print('fitness = ', self.fitness)
        fitnessFile.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + str(directOrGUI) + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
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

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[self.length, self.width, self.height])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [1.0,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[self.length, self.width, self.height])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [2.0,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[self.length, self.width, self.height])
        pyrosim.End()
        return()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+c.numSensorNeurons), weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        return()

    def Mutate(self):
        self.weights[random.randint(0,c.numSensorNeurons-1)][random.randint(0,c.numMotorNeurons-1)] = random.random() * 2 - 1

    
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        