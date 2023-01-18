import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")


    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)