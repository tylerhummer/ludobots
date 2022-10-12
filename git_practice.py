import pybullet as p
import time

physicsClient = p.connect(p.GUI)

i = 1
for i in range(1000):
    time.sleep(0.1)
    p.stepSimulation()
    print("inside loop,", i)

p.disconnect()

