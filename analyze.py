import numpy as np
import matplotlib.pyplot as plt


backLegSensorValues = np.load('data/backLeg.npy')
frontLegSensorValues = np.load('data/frontLeg.npy')

print(backLegSensorValues)
print(frontLegSensorValues)

plt.plot(backLegSensorValues, label='Back Leg', linewidth = '4')
plt.plot(frontLegSensorValues, label='Front Leg', linewidth = '2')

plt.legend()
plt.show()
