import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import random



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

length_sim = 500
backLegSensorValues = numpy.zeros(length_sim)
frontLegSensorValues = numpy.zeros(length_sim)

target = numpy.pi/2.0
targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, length_sim))

i = 1
for i in range(length_sim):
    p.stepSimulation()  #comment this out to see the starting configuration of the blocks
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform((-numpy.pi/2.0),(numpy.pi/2.0)), maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform((-numpy.pi/2.0),(numpy.pi/2.0)), maxForce=50)
    time.sleep(1/50)
print(backLegSensorValues)
print(frontLegSensorValues)

numpy.save('data/backLeg', backLegSensorValues)
numpy.save('data/frontLeg', frontLegSensorValues)
numpy.save('data/targetAngles', targetAngles)
p.disconnect()

#comment
