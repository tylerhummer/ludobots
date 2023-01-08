import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")


i = 1
for i in range(1000):
    time.sleep(1)
    print("inside loop,", i)

p.disconnect()

#comment
