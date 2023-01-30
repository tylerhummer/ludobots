from solution import SOLUTION 
from simulation import SIMULATION
import constants as c
import copy

class HILL_CLIMBER:
    
    def __init__ (self):
        self.parent = SOLUTION()

    
    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            #print('current generation ', currentGeneration)

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
        if (self.child.fitness > self.parent.fitness):
            self.parent = self.child


    def Print(self):
        print()
        print()
        print('parent fitness ', self.parent.fitness, ', child fitness ', self.child.fitness)
        print()
        print()

    def Show_Best(self):
        self.parent.Evaluate("GUI")