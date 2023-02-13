import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import randomSnakeConstants as rSC

class snakeBody:

    def __init__ (self,linkName):
        self.LinkDimensions()
        self.Sensing()
        if linkName == rSC.numLinks - 1:
            self.Final_Link(linkName)
        
        else:
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
                pyrosim.Send_Link(name=str(linkName), pos=[0, 0, 2], size=[self.length, self.width, self.height],
                           objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)

        else:
                pyrosim.Send_Link(name=str(linkName), pos=[self.length/2, 0, 0], size=[self.length,self.width,self.height],
                            objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)

    def Create_Joint (self, linkName):
        if linkName == 0:
            pyrosim.Send_Joint(name=str(linkName)+"_"+str(linkName+1), parent=str(linkName), child=str(linkName+1),
                           type="revolute", position=[(self.length/2),0, 2], jointAxis= "0 1 0")

        else:
            pyrosim.Send_Joint(name=str(linkName)+"_"+str(linkName+1), parent=str(linkName), child=str(linkName+1),
                            type="revolute", position=[self.length,0,0], jointAxis="0 1 0")

    def Final_Link (self, linkName):
        pyrosim.Send_Link(name=str(rSC.numLinks-1), pos=[self.length/2, 0, 0], size=[self.length, self.width, self.height],
                            objectType="box", mass=(self.length*self.width*self.height), sense=self.sense)