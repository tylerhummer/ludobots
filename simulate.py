import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

i = 1
for i in range(100):
    p.stepSimulation()  #comment this out to see the starting configuration of the blocks
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
print(backLegSensorValues)
print(frontLegSensorValues)

numpy.save('data/backLeg', backLegSensorValues)
numpy.save('data/frontLeg', frontLegSensorValues)
p.disconnect()

#comment
