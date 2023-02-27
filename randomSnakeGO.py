import pickle
from randomSnakePHC import PARALLEL_HILL_CLIMBER
import randomSnakeConstants as RSc

try:
    rSphc = pickle.load(open(RSc.checkpoint_file_name, "rb"))

except:
    rSphc = PARALLEL_HILL_CLIMBER()

rSphc.Evolve()
rSphc.Show_Best()
rSphc.Show_Evolution()
