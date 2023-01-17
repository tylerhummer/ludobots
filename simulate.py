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

length_sim = 1000
backLegSensorValues = numpy.zeros(length_sim)
frontLegSensorValues = numpy.zeros(length_sim)

backLeg_amplitude = numpy.pi/4
backLeg_frequency = 10
backLeg_phaseOffset = numpy.pi/8

frontLeg_amplitude = numpy.pi/4
frontLeg_frequency = 10
frontLeg_phaseOffset = 0

x_vals = numpy.linspace(0, 2*numpy.pi, length_sim)
backLeg_targetAngles = (backLeg_amplitude)*(numpy.sin(backLeg_frequency * x_vals + backLeg_phaseOffset))
frontLeg_targetAngles = (frontLeg_amplitude)*(numpy.sin(frontLeg_frequency * x_vals + frontLeg_phaseOffset))
numpy.save('data/backLeg_targetAngles', backLeg_targetAngles)
numpy.save('data/frontLeg_targetAngles', frontLeg_targetAngles)

i = 1
for i in range(length_sim):
    p.stepSimulation()  #comment this out to see the starting configuration of the blocks
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backLeg_targetAngles[i], maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontLeg_targetAngles[i], maxForce=50)
    time.sleep(1/100)
print(backLegSensorValues)
print(frontLegSensorValues)

numpy.save('data/backLeg', backLegSensorValues)
numpy.save('data/frontLeg', frontLegSensorValues)

p.disconnect()

#comment
