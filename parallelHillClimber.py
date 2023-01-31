from solution import SOLUTION 
from simulation import SIMULATION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    
    def __init__ (self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0,c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        
        for i in range(0, c.populationSize):
            self.parents[i].Evaluate("GUI")

        '''
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            #print('current generation ', currentGeneration)
        '''

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        

    def Mutate(self):
        self.child.Mutate()
       

    def Select(self):
        #print('parent fitness ', self.parent.fitness)
        if (self.child.fitness < self.parent.fitness):
            self.parent = self.child


    def Print(self):
        print()
        print()
        print('parent fitness ', self.parent.fitness, ', child fitness ', self.child.fitness)
        print()
        print()

    def Show_Best(self):
        pass
        '''
        self.parent.Evaluate("GUI")
        '''