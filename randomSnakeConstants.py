# File containing the constants for the random snake generator
import numpy
import random

# simulation setup constants

length_sim = 500

motorJointRange = 0.1

numberOfGenerations = 1
populationSize = 1

numLinks = random.randint(3,10)
numSensorNeurons = int(numLinks*random.random())
numMotorNeurons = numLinks - 1

