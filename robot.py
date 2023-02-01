import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        #os.system("del brain" + str(self.solutionID) + ".nndf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        self.robotId = p.loadURDF("body.urdf")
        


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
            

    def Sense(self, time_step):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_step)

        
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            #print(self.motors[jointName])


    def Act(self, time_step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                #print("Motorneuron", jointName, desiredAngle)
        #for i in self.motors:
            #self.motors[i].Set_Value(time_step, self.robotId)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        #print(stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        #print(xCoordinateOfLinkZero)
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        os.system("rename tmp"+str(self.solutionID)+".txt " + "fitness"+str(self.solutionID)+".txt")
        f = open("fitness" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        
# Neurons Step 30ish
