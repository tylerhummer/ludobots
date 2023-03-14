from randomSnake import SOLUTION 
from randomSnakeSimulation import SIMULATION
from randomSnakeVisualize import VISUALIZE
import randomSnakeConstants as c
import numpy
import random
import copy
import os
import pickle

class PARALLEL_HILL_CLIMBER:
    
    def __init__ (self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        os.system("del body*.urdf")
        self.fitness_time = VISUALIZE()
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        #self.Evaluate(self.parents) #***Added this line here which is the same as Evolve below to skip the evolve step!***

    def Checkpoint(self):
        self.numpyrandomstate = numpy.random.get_state()
        self.randomstate = random.getstate()
        f = open(c.checkpoint_file_name, 'wb')
        pickle.dump(self, f)
        f.close()


    def Evolve(self):
        
        self.Evaluate(self.parents)
        
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
            #print('current generation ', currentGeneration)
        

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate(currentGeneration)
        self.Evaluate(self.children)
        self.Print()
        self.Select(currentGeneration)
        self.Checkpoint()  #uncomment this to add the generations to the checkpointing file

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Mutate(self, currentGeneration):
        for i in self.children:
            #print(self.parents[i].weights)
            self.children[i].Mutate(currentGeneration)
            #print(self.children[i].weights)
       

    def Print(self):
        print()
        for i in self.parents:
            print('parent fitness ', self.parents[i].fitness, ', child fitness ', self.children[i].fitness)
        print()


    def Select(self, currentGeneration):
        #print('parent fitness ', self.parent.fitness)
        for i in self.parents:
            if (abs(self.children[i].fitness) > abs(self.parents[i].fitness)):
                self.parents[i] = self.children[i]
                selected_fitness = self.parents[i].fitness
                print("selected fitness:" + str(self.parents[i].fitness))
                self.fitness_time.Fitness_vs_Time(selected_fitness,currentGeneration)

            else:
                self.fitness_time.Fitness_vs_Time(self.parents[i].fitness,currentGeneration)


    def Show_Best(self):
        best = {}
        best = self.parents[0]
        for i in self.parents:
            if (abs(self.parents[i].fitness) > abs(best.fitness)):
                best = self.parents[i]
        print("best fitness:" + str(best.fitness))
        best.Start_Simulation("GUI")

    
    def Show_Evolution(self):
        self.fitness_time.Save()
        #self.fitness_time.Plot() #uncomment to check to see if it looks like what is expected

        

    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT") #change DIRECT to GUI to see body orientation... set number of gens and pop to 1 to not crash computer

        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()