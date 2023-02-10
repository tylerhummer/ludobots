import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import randomSnakeConstants as rSC

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(rSC.numSensorNeurons, rSC.numMotorNeurons)
        self.weights = self.weights * 2 - 1

        self.myID = nextAvailableID
        print("My ID: " + str(self.myID) + " My weights:")
        print(self.weights)

    
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
        return

    def Create_Snake(self):
        pass

    def Create_Snake_Brain(self):
        pass


    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()
        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        pass

    def Mutate_Brain(self):
        pass

    def Mutate_Body(self):
        pass

    def Set_ID(self, nextAvailableID):
        pass

