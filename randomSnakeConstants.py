# File containing the constants for the random snake generator
import numpy
import random

# simulation setup constants

length_sim = 1000

motorJointRange = 0.3

numberOfGenerations = 1
populationSize = 1

numLinks = random.randint(5,12)
numSensorNeurons = int(numLinks*random.uniform(0.25,0.75))
numMotorNeurons = numLinks

