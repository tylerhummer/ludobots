# File containing the constants for the random snake generator
import numpy
import random

# simulation setup constants

length_sim = 1500

motorJointRange = 0.3

numberOfGenerations = 1
populationSize = 1

numLinks = 10
numSensorNeurons = 5
numMotorNeurons = numLinks - 1

seed_number = 7760
checkpoint_file_name = "checkpoint_seed" + str(seed_number) + ".pkl"
csv_file_name = "seed_" + str(seed_number) + ".csv"


