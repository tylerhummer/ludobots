import pyrosim.pyrosim as pyrosim
import numpy
import randomSnakeConstants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        #print(self.linkName)
        self.values = numpy.zeros(c.length_sim)


    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        #t = time_step
        #if t == (c.length_sim-1): 
        #    print(self.values)

    def Save_Value(self, linkName):
        numpy.save('data/' f'{linkName}', self.values)
        #numpy.save('data/frontLeg', c.frontLegSensorValues)
