import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import randomSnakeConstants as rSC

class SnakeBody:

    def __init__ (self,linkName):
        self.LinkDimensions()
        self.Sensing()
        if linkName == rSC.numLinks - 1:
            self.Final_Link(linkName)
        
        else:
            self.linkName = ("Link" +str(linkName))
            self.nextLinkName = ("Link" + str(linkName+1))
            self.jointName = ("Link" + str(linkName)+"_" + "Link" + str(linkName+1))
            self.Create_Link(linkName)
            self.Create_Joint(linkName)
        

    def LinkDimensions (self):
        self.length = random.uniform(0.5, 1)
        self.width = random.uniform(0.5, 1)
        self.height = random.uniform(0.5, 1)

    def Sensing (self):
        self.sense = random.randint(0, 1)
        

    def Create_Link (self, linkName):
        if linkName == 0:
                pyrosim.Send_Link(name=self.linkName, pos=[0, 0, 2], size=[self.length, self.width, self.height],
                           objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)

        else:
                pyrosim.Send_Link(name=self.linkName, pos=[self.length/2, 0, 0], size=[self.length,self.width,self.height],
                            objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)

    def Create_Joint (self, linkName):
        if linkName == 0:
            pyrosim.Send_Joint(name=self.jointName, parent=self.linkName, child=self.nextLinkName,
                           type="revolute", position=[(self.length/2),0, 2], jointAxis= "0 1 0")

        else:
            pyrosim.Send_Joint(name=self.jointName, parent=self.linkName, child=self.nextLinkName,
                            type="revolute", position=[self.length,0,0], jointAxis="0 1 0")

    def Final_Link (self, linkName):
        self.linkName = ("Link"+ str(rSC.numLinks-1))
        pyrosim.Send_Link(name=self.linkName, pos=[self.length/2, 0, 0], size=[self.length, self.width, self.height],
                            objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)

    def Create_Sensing_Neuron(self):
        pass

    def Create_Motor_Neuron(self):
        pass