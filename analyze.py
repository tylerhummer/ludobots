import numpy as np
import matplotlib.pyplot as plt


backLegSensorValues = np.load('data/backLeg.npy')
frontLegSensorValues = np.load('data/frontLeg.npy')
targetAngles = np.load('data/targetAngles.npy')
'''
print(backLegSensorValues)
print(frontLegSensorValues)

plt.figure(1)
plt.plot(backLegSensorValues, label='Back Leg', linewidth = '4')
plt.plot(frontLegSensorValues, label='Front Leg', linewidth = '2')
plt.legend()
'''

plt.figure(2)
plt.plot(targetAngles, label="Sine Function", linewidth='3')
plt.legend()

plt.show()
