import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
from simulation import SIMULATION
import sys


directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
'''
robotId = p.loadURDF("body.urdf")

numpy.save('data/backLeg_targetAngles', c.backLeg_targetAngles)
numpy.save('data/frontLeg_targetAngles', c.frontLeg_targetAngles)

i = 1
for i in range(c.length_sim):
    p.stepSimulation()  #comment this out to see the starting configuration of the blocks
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.backLeg_targetAngles[i], maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.frontLeg_targetAngles[i], maxForce=50)
    time.sleep(1/100)
print(c.backLegSensorValues)
print(c.frontLegSensorValues)

numpy.save('data/backLeg', c.backLegSensorValues)
numpy.save('data/frontLeg', c.frontLegSensorValues)

'''