import numpy
import matplotlib.pyplot as plt
import pandas as pd
import randomSnakeConstants as RSc

class VISUALIZE:

    def __init__ (self):
        self.running_max = numpy.array([0,0]).reshape(2,1)
        print(self.running_max)

    
    def Fitness_vs_Time (self, selectedFitness, currentGeneration):
        if numpy.abs(selectedFitness) > max(numpy.abs(self.running_max[1])):
            add = numpy.array([currentGeneration, numpy.abs(selectedFitness)]).reshape(2,1)
            self.running_max = numpy.append(self.running_max, add,axis=1)
        else:
            pass
            #add = numpy.array([currentGeneration, max(self.running_max[1])]).reshape(2,1)
            #self.running_max = numpy.append(self.running_max, add, axis=1)

        print(self.running_max)

    def Plot (self):
        plt.title("Evolved Fitness") 
        plt.xlabel("Generations") 
        plt.ylabel("Fitness") 
        plt.plot(self.running_max[0],self.running_max[1]) 
        plt.show() 

    def Save (self):
        transposed = self.running_max.T
        numpy.savetxt(RSc.csv_file_name, transposed, delimiter = ',')

