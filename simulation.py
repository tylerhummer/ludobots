import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import constants as c
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        #pyrosim.Prepare_To_Simulate(robotId)


        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        i = 1
        for i in range(c.length_sim):
            print(i)
            p.stepSimulation()  #comment this out to see the starting configuration of the blocks
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.backLeg_targetAngles[i], maxForce=50)
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.frontLeg_targetAngles[i], maxForce=50)
            time.sleep(1/60)

    def __del__(self):
        p.disconnect()