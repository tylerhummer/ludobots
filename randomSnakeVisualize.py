import numpy
import matplotlib.pyplot as plt
import randomSnakeConstants as RSc

class VISUALIZE:

    def __init__ (self):
        self.running_max = numpy.array([0,0]).reshape(2,1)
        #print(self.running_max)

    
    def Fitness_vs_Time (self, selectedFitness, currentGeneration):
        if numpy.abs(selectedFitness) > max(numpy.abs(self.running_max[1])):
            add = numpy.array([currentGeneration, numpy.abs(selectedFitness)]).reshape(2,1)
            self.running_max = numpy.append(self.running_max, add,axis=1)
        else:
            add = numpy.array([currentGeneration, max(numpy.abs(self.running_max[1]))]).reshape(2,1)
            if add[0] in self.running_max:
                pass
            else:
                self.running_max = numpy.append(self.running_max, add, axis=1)
            #add = numpy.array([currentGeneration, max(self.running_max[1])]).reshape(2,1)
            #self.running_max = numpy.append(self.running_max, add, axis=1)

        #print(self.running_max)

    def Save (self):
        transposed = self.running_max.T
        numpy.savetxt(RSc.csv_file_name, transposed, delimiter = ',')

