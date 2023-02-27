import csv
import matplotlib.pyplot as plt

x_1 = []
y_1 = []

with open('seed_5.csv', 'r') as csvfile:
    plot = csv.reader(csvfile, delimiter = ',')

    for rows in plot:
        x_1.append(rows[0])
        y_1.append(float(rows[1]))


plt.title("Evolved Fitness") 
plt.xlabel("Generations") 
plt.ylabel("Fitness") 
plt.plot(x_1,y_1) 
plt.show()