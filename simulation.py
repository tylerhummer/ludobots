import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        #pyrosim.Prepare_To_Simulate(robotId)

        self.world = WORLD()
        self.robot = ROBOT()


    def __del__(self):
        p.disconnect()