# File containing the constants for the random snake generator
import numpy
import random

# simulation setup constants

length_sim = 1000

motorJointRange = 0.3

numberOfGenerations = 5
populationSize = 5

numLinks = 10
numSensorNeurons = 5
numMotorNeurons = numLinks - 1

seed_number = 5
checkpoint_file_name = "checkpoint_seed" + str(seed_number) + ".pkl"
csv_file_name = "seed_" + str(seed_number) + ".csv"


