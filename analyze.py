import numpy as np
import matplotlib.pyplot as plt


backLegSensorValues = np.load('data/backLeg.npy')
frontLegSensorValues = np.load('data/frontLeg.npy')
backLegtargetAngles = np.load('data/backLeg_targetAngles.npy')
frontLegtargetAngles = np.load('data/frontLeg_targetAngles.npy')
'''
print(backLegSensorValues)
print(frontLegSensorValues)

plt.figure(1)
plt.plot(backLegSensorValues, label='Back Leg', linewidth = '4')
plt.plot(frontLegSensorValues, label='Front Leg', linewidth = '2')
plt.legend()
'''

plt.figure(2)
plt.plot(backLegtargetAngles, label="Back Leg Motor Values", linewidth='5')
plt.plot(frontLegtargetAngles, label="Front Leg Motor Values", linewidth='2')
plt.legend()

plt.show()
