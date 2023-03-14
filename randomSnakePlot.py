import os
import pandas as pd
import matplotlib.pyplot as plt

### Set your path to the folder containing the .csv files
PATH = "C:/Users/17thu/Documents/GitHub/ludobots./" #Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

### Loop over all files
for file in fileNames:

    ### Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col = 0)
    label_name = str(file)
    ### Create line for every file
    plt.plot(df, label = label_name.removesuffix('.csv'))
    
plt.title("Evolutionary Improvement")
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.legend(loc = "best")
### Generate the plot
plt.show()