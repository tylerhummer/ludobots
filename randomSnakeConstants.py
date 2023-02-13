# File containing the constants for the random snake generator
import numpy
import random

# simulation setup constants

length_sim = 500

motorJointRange = 0.3

numberOfGenerations = 1
populationSize = 1

numLinks = random.randint(3,10)
numSensorNeurons = int(numLinks*random.uniform(0.25,0.75))
numMotorNeurons = numLinks

