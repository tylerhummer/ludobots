# A file containing all the constants being used in the various simulations for ludobots

import numpy
import random


# simulation setup constants

length_sim = 300
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
