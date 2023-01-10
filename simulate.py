import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


i = 1
for i in range(2000):
    p.stepSimulation()  #comment this out to see the starting configuration of the blocks
    time.sleep(1/60)
    print("inside loop,", i)

p.disconnect()

#comment
