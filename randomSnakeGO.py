import pickle
from randomSnakePHC import PARALLEL_HILL_CLIMBER
import randomSnakeConstants as RSc
import numpy
import random

try:
    rSphc = pickle.load(open(RSc.checkpoint_file_name, "rb"))
    random.setstate(rSphc.randomstate)
    numpy.random.set_state(rSphc.numpyrandomstate)

except:
    random.seed(RSc.seed_number)
    numpy.random.seed(RSc.seed_number)
    rSphc = PARALLEL_HILL_CLIMBER()

rSphc.Evolve()
#input("Press Enter to Continue")
rSphc.Show_Best()
#input("Press Enter to Continue")
rSphc.Show_Evolution()
