import pybullet as p
import time

physicsClient = p.connect(p.GUI)

i = 1
for i in range(1000):
    time.sleep(1)
    print("inside loop,", i)

p.disconnect()

