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

        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))
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

    def Create_Snake(self):
        pyrosim.Start_URDF("body.urdf")

        

        #create the other randomly placed joints in a snake pattern
        for linkName in range(rSC.numLinks):
            length = random.uniform(0.5, 1)
            width = random.uniform(0.5, 1)
            height = random.uniform(0.5, 1)
            sensor = random.randint(0, 1)

            #create the seed link and joint
            if linkName == 0:
                pyrosim.Send_Link(name=str(linkName), pos=[0, 0, 2], size=[length, width, height],
                           objectType="box", mass=(length*width*height), sense=sensor)
                pyrosim.Send_Joint(name=str(linkName)+"_"+str(linkName+1), parent=str(linkName), child=str(linkName+1),
                           type="revolute", position=[(length/2),0, 2], jointAxis= "0 1 0")

            #create the other randomly placed joints in a snake pattern
            else:
                pyrosim.Send_Link(name=str(linkName), pos=[length/2, 0, 0], size=[length,width,height],
                            objectType="box", mass=(length*width*height), sense=sensor)
                pyrosim.Send_Joint(name=str(linkName)+"_"+str(linkName+1), parent=str(linkName), child=str(linkName+1),
                            type="revolute", position=[length,0,0], jointAxis="0 1 0")
        
        pyrosim.Send_Link(name=str(rSC.numLinks), pos=[length/2, 0, 0], size=[random.uniform(0.5, 1),random.uniform(0.5, 1),random.uniform(0.5, 1)],
                            objectType="box", mass=(length*width*height), sense=sensor)
        
        pyrosim.End()
        return()

    def Create_Snake_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.End()
        return()



    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Snake()
        self.Create_Snake_Brain()
        os.system("start /B python randomSnakeSimulate.py " + str(directOrGUI) + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.1)
        fitnessFile = open("fitness" + str(self.myID) + ".txt","r")
        self.fitness = float(fitnessFile.read())
        print('fitness = ', self.fitness)
        fitnessFile.close()

    def Mutate_Brain(self):
        pass

    def Mutate_Body(self):
        pass

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

