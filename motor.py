import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        print(self.jointName)
        self.motor_Values = numpy.zeros(c.length_sim)
        print(self.motor_Values)
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.backLeg_amplitude
        self.frequency = c.backLeg_frequency
        self.offset = c.backLeg_phaseOffset
        self.motor_Values = (self.amplitude)*(numpy.sin(self.frequency * c.x_vals + self.offset))
        print(self.motor_Values)
        #frontLeg_targetAngles = (frontLeg_amplitude)*(numpy.sin(frontLeg_frequency * x_vals + frontLeg_phaseOffset))
        #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName =self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = c.backLeg_targetAngles[i], maxForce=50)
        #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.frontLeg_targetAngles[i], maxForce=50)
        #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.backLeg_targetAngles[i], maxForce=50)
        #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.frontLeg_targetAngles[i], maxForce=50)


    def Set_Value(self, time_step, robotId):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName =self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motor_Values[time_step], maxForce=50)
