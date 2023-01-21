import pyrosim.pyrosim as pyrosim
import numpy
import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        print(self.linkName)
        self.values = numpy.zeros(c.length_sim)
        print(self.values)


    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #print(self.values)