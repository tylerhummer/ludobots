# A file containing all the constants being used in the various simulations for ludobots

import numpy
import random


# simulation setup constants

length_sim = 1000
#backLegSensorValues = numpy.zeros(length_sim)
#frontLegSensorValues = numpy.zeros(length_sim)

backLeg_amplitude = numpy.pi/4
backLeg_frequency = 10
backLeg_phaseOffset = numpy.pi/8

frontLeg_amplitude = numpy.pi/4
frontLeg_frequency = 10
frontLeg_phaseOffset = 0

x_vals = numpy.linspace(0, 2*numpy.pi, length_sim)
backLeg_targetAngles = (backLeg_amplitude)*(numpy.sin(backLeg_frequency * x_vals + backLeg_phaseOffset))
frontLeg_targetAngles = (frontLeg_amplitude)*(numpy.sin(frontLeg_frequency * x_vals + frontLeg_phaseOffset))

motorJointRange = 0.1

numberOfGenerations = 2
populationSize = 2

#numSensorNeurons = 10
#numMotorNeurons = 9


#Crab Constants
numSensorNeurons = 19
numMotorNeurons = 18

#Crab Body Dimension Stuff
crabTorsoLength = 1.5
crabTorsoWidth = 1
crabTorsoDepth = 1

crabLegLength = 1
crabLegWidth = 0.2
crabLegDepth = 0.2

crabClawLength = 0.4
crabClawWidth = 0.1
crabClawDepth = 0.1
