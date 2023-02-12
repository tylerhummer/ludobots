import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
from randomSnakeSimulation import SIMULATION
import sys


directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
