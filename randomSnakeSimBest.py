import pickle
from randomSnakePHC import PARALLEL_HILL_CLIMBER
import randomSnakeConstants as RSc
import numpy
import random


rSphc = pickle.load(open(RSc.checkpoint_file_name, "rb"))
random.setstate(rSphc.randomstate)
numpy.random.set_state(rSphc.numpyrandomstate)

rSphc.Show_Best()


