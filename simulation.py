import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
from world import WORLD
from robot import ROBOT



class SIMULATION:
    def __init__(self, directOrGUI):
        print(directOrGUI)
        if (directOrGUI == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()


    def Run(self):
        time_step = 1
        for time_step in range(c.length_sim):
            #print("time step", time_step)
            p.stepSimulation()  #comment this out to see the starting configuration of the blocks
            self.robot.Sense(time_step)
            self.robot.Think()
            self.robot.Act(time_step)
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.backLeg_targetAngles[i], maxForce=50)
            #pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName ='Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = c.frontLeg_targetAngles[i], maxForce=50)
            time.sleep(1/30)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()