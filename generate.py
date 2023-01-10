import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1


for i in range (5):
    for j in range (5):
        length = 1
        width = 1
        height = 1
        for k in range (10):
            x = i
            y = j
            z = 0.5 + k

            pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length, width, height])

            length = length * 0.9 
            width = width * 0.9
            height = height * 0.9
            
            
            print("i = ",i)
            print("j = ",j)
            print("k = ",k)

pyrosim.End()