import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):
        #self.objects = p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")