import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.robotId = p.loadURDF("body.urdf")


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
            

    def Sense(self, time_step):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_step)
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #self.sensors.Print_Values()

        
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            #print(self.motors[jointName])


    def Act(self, time_step):
        for i in self.motors:
            self.motors[i].Set_Value(time_step, self.robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
# Neurons Step 30ish
