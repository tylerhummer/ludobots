import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import randomSnakeConstants as rSC

class  SnakeBody:

    def __init__ (self,linkName,prevFace,prevDimensions):
        self.LinkDimensions()
        self.Sensing()
        self.Face(prevFace, prevDimensions)
        self.Mass()
        self.Joint_Orientation()
        if linkName == rSC.numLinks - 1:
            self.Final_Link(linkName)
        
        else:
            self.linkName = ("Link" +str(linkName))
            self.nextLinkName = ("Link" + str(linkName+1))
            self.jointName = ("Link" + str(linkName)+"_" + "Link" + str(linkName+1))
            self.Create_Link(linkName)
            self.Create_Joint(linkName)
        

    def LinkDimensions (self):
        self.dimensions = numpy.random.uniform(0.25, 1.25,3)
        

    def Sensing (self):
        self.sense = random.randint(0, 1)
        
    def Face(self,prevFace, prevDimensions):
        self.faceNum = random.randint(0,5)
        while (self.faceNum+prevFace) == 5: #Loop to make sure the next link isn't sent back to the same spot
            self.faceNum = random.randint(0,5)
        
        link = [[-0.5,0,0], [0,0,0.5], [0,-0.5,0], [0,0.5,0], [0,0,-0.5],[0.5,0,0]] #link depends only on previous face
        
        if prevFace == 0: #If prev_face is left face, then send next link and joint to index of faceNum
            joint = [[-1,0,0], [-0.5,0,0.5], [-0.5,-0.5,0], [-0.5,0.5,0], [-0.5,0,-0.5],[0,0,0]]

        elif prevFace == 1: #If prev_face is top face, then send next link and joint to index of faceNum
            joint = [[-0.5,0,0.5], [0,0,1], [0,-0.5,0.5], [0,0.5,0.5], [0,0,0],[0.5,0,0.5]]

        elif prevFace == 2: #If prev_face is front face, then send next link and joint to index of faceNum
            joint = [[-0.5,-0.5,0], [0,-0.5,0.5], [0,-1,0], [0,0,0], [0,-0.5,-0.5],[0.5,-0.5,0]]

        elif prevFace == 3: #If prev_face is back face, then send next link and joint to index of faceNum
            joint = [[-0.5,0.5,0], [0,0.5,0.5], [0,0,0], [0,1,0], [0,0.5,-0.5],[0.5,0.5,0]]

        elif prevFace == 4: #If prev_face is back face, then send next link and joint to index of faceNum
            joint = [[-0.5,0,-0.5], [0,0,0], [0,-0.5,-0.5], [0,0.5,-0.5], [0,0,-1],[0.5,0,-0.5]]

        else: #If prev_face is right face, then send next link and joint to index of faceNum
            joint = [[0,0,0], [0.5,0,0.5], [0.5,-0.5,0], [0.5,0.5,0], [0.5,0,-0.5],[1,0,0]]

        self.linkPos = link[prevFace]*self.dimensions
        self.jointPos = joint[self.faceNum]*self.dimensions
        
    def Joint_Orientation(self):
        orient = random.randint(0,2)
        
        if orient == 0: 
            self.jointOrientation = "1 0 0"

        elif orient == 1:
            self.jointOrientation = "0 1 0"

        else: 
            self.jointOrientation = "0 0 1"

    def Mass(self):
        self.mass = self.dimensions[0]*self.dimensions[1]*self.dimensions[2]

    def Create_Link (self, linkName):
        if linkName == 0: #Set the location of the seed link to a specific known
                self.faceNum = 5
                pyrosim.Send_Link(name=self.linkName, pos=[0, 0, 2], size = [self.dimensions[0],self.dimensions[1],self.dimensions[2]],
                           objectType="box", mass=(self.mass), sense=self.sense)

        elif linkName == 1: #Set the location of the second link
                pyrosim.Send_Link(name=self.linkName, pos=[self.dimensions[0]/2,0,0], size = [self.dimensions[0],self.dimensions[1],self.dimensions[2]],
                           objectType="box", mass=(self.mass), sense=self.sense)

        else:
                pyrosim.Send_Link(name=self.linkName, pos=[self.linkPos[0],self.linkPos[1],self.linkPos[2]], size = [self.dimensions[0],self.dimensions[1],self.dimensions[2]],
                            objectType="box", mass=(self.mass), sense=self.sense)

    def Create_Joint (self, linkName):
        if linkName == 0:
            pyrosim.Send_Joint(name=self.jointName, parent=self.linkName, child=self.nextLinkName,
                           type="revolute", position=[(self.dimensions[0]/2),0, 2], jointAxis= "1 0 0")

        else:
            pyrosim.Send_Joint(name=self.jointName, parent=self.linkName, child=self.nextLinkName,
                            type="revolute", position=[self.jointPos[0], self.jointPos[1], self.jointPos[2]], jointAxis=self.jointOrientation)

    def Final_Link (self,linkName):
        self.linkName = ("Link"+ str(rSC.numLinks-1))
        pyrosim.Send_Link(name=self.linkName, pos=[self.linkPos[0],self.linkPos[1],self.linkPos[2]], size = [self.dimensions[0],self.dimensions[1],self.dimensions[2]],
                            objectType="box", mass=(self.mass), sense=self.sense)

    def Create_Sensing_Neuron(self):
        pass

    def Create_Motor_Neuron(self):
        pass