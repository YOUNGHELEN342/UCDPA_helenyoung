#   This function achieves the following learning outcomes :
#       2. Importing data
#       3. Analysing data

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import json

print(os.getcwd())
# Import CSV file from Kaggle
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")
#Dropped ID as not required.
data= data.drop(["id"], axis=1)

print(data.isnull().sum())

# Elimination of null values that I saw in BMI.
data= data.dropna(subset=['bmi'], axis=0)

#To remove 1 line as "Other" in Gender.
lines_drop= data[data["gender"] =="Other"].index
data.drop(lines_drop,inplace=True)


np.values= data.values
print(np.values)

















