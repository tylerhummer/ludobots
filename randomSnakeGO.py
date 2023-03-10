import pickle
from randomSnakePHC import PARALLEL_HILL_CLIMBER
import randomSnakeConstants as RSc
import numpy
import random

try:
    rSphc = pickle.load(open(RSc.checkpoint_file_name, "rb"))

except:
    random.seed(1)
    numpy.random.seed(1)
    rSphc = PARALLEL_HILL_CLIMBER()

rSphc.Evolve()
#input("Press Enter to Continue")
rSphc.Show_Best()
#input("Press Enter to Continue")
rSphc.Show_Evolution()
