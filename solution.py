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
        self.legLength = 1
        self.legWidth = 0.2
        self.legDepth = 0.2
        
        self.myID = nextAvailableID
        print("My ID: " + str(self.myID) + " My weights:")
        print(self.weights)

    def Evaluate(self, directOrGUI):
        self.Create_World()
        #self.Create_Body()
        #self.Create_Brain()
        self.Create_Crab()
        self.Create_Crab_Brain()
        os.system("start /B python simulate.py " + str(directOrGUI) + " " + str(self.myID))
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read())
        print('fitness = ', self.fitness)
        fitnessFile.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Crab()
        self.Create_Crab_Brain()
        #self.Create_Body()
        #self.Create_Brain()
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
        pyrosim.Send_Sphere(name="BallA", pos=[-0.25,+0.25,4], size=[0.25])
        pyrosim.Send_Sphere(name="BallB", pos=[-0.5,+0.5,6], size=[0.25])
        pyrosim.Send_Sphere(name="BallC", pos=[-0.75,+0.25,6], size=[0.25])
        pyrosim.Send_Sphere(name="BallD", pos=[+0.25,+0.5,7], size=[0.25])
        #pyrosim.Send_Cube(name="bowlingPin", pos=[-3,-2,0.5], size=[self.legWidth,self.legDepth,self.legLength])
        pyrosim.End()
        return

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Link(name="Torso", pos=[0,0,1], size=[self.length, self.width, self.height], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [0,-0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="BackLeg", pos=[0,-0.5,0], size=[self.legWidth, self.legLength, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "BackLeg_LowerBackLeg", parent = "BackLeg", child = "LowerBackLeg", type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="LowerBackLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [0,0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="FrontLeg", pos=[0,0.5,0], size=[self.legWidth, self.legLength, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "FrontLeg_LowerFrontLeg", parent = "FrontLeg", child = "LowerFrontLeg", type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="LowerFrontLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [0.5,0,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="RightLeg", pos=[0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "RightLeg_LowerRightLeg", parent = "RightLeg", child = "LowerRightLeg", type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerRightLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-0.5,0,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LeftLeg", pos=[-0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "LeftLeg_LowerLeftLeg", parent = "LeftLeg", child = "LowerLeftLeg", type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerLeftLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.End()
        return()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LowerRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 13, jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron(name = 14, jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name = 15, jointName = "RightLeg_LowerRightLeg")
        pyrosim.Send_Motor_Neuron(name = 16, jointName = "LeftLeg_LowerLeftLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+c.numSensorNeurons), weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        return()

    def Mutate(self):
        self.weights[random.randint(0,c.numSensorNeurons-1)][random.randint(0,c.numMotorNeurons-1)] = random.random() * 2 - 1

    
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        
    
    def Create_Crab(self):
        pyrosim.Start_URDF("body1.urdf")
        pyrosim.Send_Link(name="Torso", pos=[0,0,1], size=[c.crabTorsoDepth, c.crabTorsoLength, c.crabTorsoWidth], objectType="box", mass=10.0)
        pyrosim.Send_Joint(name = "Torso_FrontRightLeg", parent = "Torso", child = "FrontRightLeg", type = "revolute", position = [0.5,0.5,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="FrontRightLeg", pos=[0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "FrontRightLeg_LowerFrontRightLeg", parent = "FrontRightLeg", child = "LowerFrontRightLeg", type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerFrontRightLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_FrontLeftLeg", parent = "Torso", child = "FrontLeftLeg", type = "revolute", position = [-0.5,0.5,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="FrontLeftLeg", pos=[-0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "FrontLeftLeg_LowerFrontLeftLeg", parent = "FrontLeftLeg", child = "LowerFrontLeftLeg", type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerFrontLeftLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_MiddleRightLeg", parent = "Torso", child = "MiddleRightLeg", type = "revolute", position = [0.5,0,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="MiddleRightLeg", pos=[0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "MiddleRightLeg_LowerMiddleRightLeg", parent = "MiddleRightLeg", child = "LowerMiddleRightLeg", type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerMiddleRightLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_MiddleLeftLeg", parent = "Torso", child = "MiddleLeftLeg", type = "revolute", position = [-0.5,0,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="MiddleLeftLeg", pos=[-0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "MiddleLeftLeg_LowerMiddleLeftLeg", parent = "MiddleLeftLeg", child = "LowerMiddleLeftLeg", type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerMiddleLeftLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_BackRightLeg", parent = "Torso", child = "BackRightLeg", type = "revolute", position = [0.5,-0.5,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="BackRightLeg", pos=[0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "BackRightLeg_LowerBackRightLeg", parent = "BackRightLeg", child = "LowerBackRightLeg", type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerBackRightLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_BackLeftLeg", parent = "Torso", child = "BackLeftLeg", type = "revolute", position = [-0.5,-0.5,1.0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="BackLeftLeg", pos=[-0.5,0,0], size=[self.legLength, self.legWidth, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "BackLeftLeg_LowerBackLeftLeg", parent = "BackLeftLeg", child = "LowerBackLeftLeg", type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="LowerBackLeftLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)

        pyrosim.Send_Joint(name = "Torso_FrontRightArm", parent = "Torso", child = "FrontRightArm", type = "revolute", position = [0.25,0.5,1.25], jointAxis = "0 0 1")
        pyrosim.Send_Link(name="FrontRightArm", pos=[0,0.5,0], size=[self.legWidth, self.legLength, self.legDepth], objectType="box", mass=0.5)
        pyrosim.Send_Joint(name = "FrontRightArm_FrontRightClaw", parent = "FrontRightArm", child = "FrontRightClaw", type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="FrontRightClaw", pos=[0,0,0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=0.25)
        pyrosim.Send_Joint(name = "FrontRightClaw_FrontRightClawTip", parent = "FrontRightClaw", child = "FrontRightClawTip", type = "revolute", position = [0,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="FrontRightClawTip", pos=[0,-0.2,0], size=[c.crabClawWidth, c.crabClawLength, c.crabClawDepth], objectType="box", mass=0.25)

        pyrosim.Send_Joint(name = "Torso_FrontLeftArm", parent = "Torso", child = "FrontLeftArm", type = "spherical", position = [-0.25 ,0.5,1.25], jointAxis = "0 0 1")
        pyrosim.Send_Link(name="FrontLeftArm", pos=[0,0.5,0], size=[self.legWidth, self.legLength, self.legDepth], objectType="box", mass=0.5)
        pyrosim.Send_Joint(name = "FrontLeftArm_FrontLeftClaw", parent = "FrontLeftArm", child = "FrontLeftClaw", type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
        pyrosim.Send_Link(name="FrontLeftClaw", pos=[0,0,0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=0.25)
        pyrosim.Send_Joint(name = "FrontLeftClaw_FrontLeftClawTip", parent = "FrontLeftClaw", child = "FrontLeftClawTip", type = "revolute", position = [0,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="FrontLeftClawTip", pos=[0,-0.2,0], size=[c.crabClawWidth, c.crabClawLength, c.crabClawDepth], objectType="box", mass=0.25)
        
        '''
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position = [0,0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="FrontLeg", pos=[0,0.5,0], size=[self.legWidth, self.legLength, self.legDepth], objectType="box", mass=1.0)
        pyrosim.Send_Joint(name = "FrontLeg_LowerFrontLeg", parent = "FrontLeg", child = "LowerFrontLeg", type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Link(name="LowerFrontLeg", pos=[0,0,-0.5], size=[self.legWidth, self.legDepth, self.legLength], objectType="box", mass=1.0)
        '''
        pyrosim.End()
        return()

    def Create_Crab_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "MiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "MiddleLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LowerFrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "LowerFrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 9, linkName = "LowerMiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 10, linkName = "LowerMiddleLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 11, linkName = "LowerBackRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 12, linkName = "LowerBackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 13, linkName = "FrontRightArm")
        pyrosim.Send_Sensor_Neuron(name = 14, linkName = "FrontRightClaw")
        pyrosim.Send_Sensor_Neuron(name = 15, linkName = "FrontRightClawTip")
        pyrosim.Send_Sensor_Neuron(name = 16, linkName = "FrontLeftArm")
        pyrosim.Send_Sensor_Neuron(name = 17, linkName = "FrontLeftClaw")
        pyrosim.Send_Sensor_Neuron(name = 18, linkName = "FrontLeftClawTip")
        pyrosim.Send_Motor_Neuron(name = 19, jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron(name = 20, jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 21, jointName = "Torso_MiddleRightLeg")
        pyrosim.Send_Motor_Neuron(name = 22, jointName = "Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 23, jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron(name = 24, jointName = "Torso_BackLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 25, jointName = "FrontRightLeg_LowerFrontRightLeg")
        pyrosim.Send_Motor_Neuron(name = 26, jointName = "FrontLeftLeg_LowerFrontLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 27, jointName = "MiddleRightLeg_LowerMiddleRightLeg")
        pyrosim.Send_Motor_Neuron(name = 28, jointName = "MiddleLeftLeg_LowerMiddleLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 29, jointName = "BackRightLeg_LowerBackRightLeg")
        pyrosim.Send_Motor_Neuron(name = 30, jointName = "BackLeftLeg_LowerBackLeftLeg")
        pyrosim.Send_Motor_Neuron(name = 31, jointName = "Torso_FrontRightArm")
        pyrosim.Send_Motor_Neuron(name = 32, jointName = "FrontRightArm_FrontRightClaw")
        pyrosim.Send_Motor_Neuron(name = 33, jointName = "FrontRightClaw_FrontRightClawTip")
        pyrosim.Send_Motor_Neuron(name = 34, jointName = "Torso_FrontLeftArm")
        pyrosim.Send_Motor_Neuron(name = 35, jointName = "FrontLeftArm_FrontLeftClaw")
        pyrosim.Send_Motor_Neuron(name = 36, jointName = "FrontLeftClaw_FrontLeftClawTip")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = (currentColumn+c.numSensorNeurons), weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        return()