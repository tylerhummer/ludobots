import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import randomSnakeConstants as rSC
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import math


class ROBOT:
    def __init__(self, solutionID, world):
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        #os.system("del brain" + str(self.solutionID) + ".nndf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        self.robotId = p.loadURDF("body" + str(self.solutionID) + ".urdf")
        self.world = world
        


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
                desiredAngle = (self.nn.Get_Value_Of(neuronName)) * rSC.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
                #print("Motorneuron", jointName, desiredAngle)
        #for i in self.motors:
            #self.motors[i].Set_Value(time_step, self.robotId)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        '''
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        ballAPositionAndOrientation = p.getBasePositionAndOrientation(self.world.objects[0])
        ballBPositionAndOrientation = p.getBasePositionAndOrientation(self.world.objects[1])
        ballCPositionAndOrientation = p.getBasePositionAndOrientation(self.world.objects[2])
        ballDPositionAndOrientation = p.getBasePositionAndOrientation(self.world.objects[3])
        #print(stateOfLinkZero)
        basePosition = basePositionAndOrientation[0]
        ballAPosition = ballAPositionAndOrientation[0]
        ballBPosition = ballBPositionAndOrientation[0]
        ballCPosition = ballCPositionAndOrientation[0]
        ballDPosition = ballDPositionAndOrientation[0]
        #print(positionOfLinkZero)
        yPosition = basePosition[1]
        ballAHeight = ballAPosition[2]
        ballBHeight = ballBPosition[2]
        ballCHeight = ballCPosition[2]
        ballDHeight = ballDPosition[2]
        #print(xCoordinateOfLinkZero)
        #fitness = xPosition
        '''
        #fitness = ballAHeight + ballBHeight + ballCHeight + ballDHeight + (5 * yPosition)
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #print(basePositionAndOrientation)
        basePosition = basePositionAndOrientation[0]
        #print(basePosition)
        xPosition = basePosition[0]
        #print(xPosition)
        zPosition = basePosition[2]
        #print(zPosition)

        if zPosition > 2:
            fitness = 0

        else:
            fitness = xPosition
        
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        os.system("rename tmp"+str(self.solutionID)+".txt " + "fitness"+str(self.solutionID)+".txt")
        f = open("fitness" + str(self.solutionID) + ".txt", "w")
        f.write(str(fitness))
        f.close()
        
# Neurons Step 30ish
