from solution import SOLUTION 
from simulation import SIMULATION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    
    def __init__ (self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        
        self.Evaluate(self.parents)
        
        '''
        for i in range(0, c.populationSize):
            self.parents[i].Start_Simulation("DIRECT")

        for i in range(0, c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()
        '''
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            #print('current generation ', currentGeneration)
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
       

    def Print(self):
        print()
        for i in self.parents:
            print('parent fitness ', self.parents[i].fitness, ', child fitness ', self.children[i].fitness)
        print()


    def Select(self):
        #print('parent fitness ', self.parent.fitness)
        for i in self.parents:
            if (self.children[i].fitness < self.parents[i].fitness):
                self.parents[i] = self.children[i]


    def Show_Best(self):
        best = {}
        best = self.parents[0]
        for i in self.parents:
            if (self.parents[i].fitness < best.fitness):
                best = self.parents[i]
        print(best.fitness)
        best.Start_Simulation("GUI")
        

    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT") #change DIRECT to GUI to see body orientation... set number of gens and pop to 1 to not crash computer

        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()