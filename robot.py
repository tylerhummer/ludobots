import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
            