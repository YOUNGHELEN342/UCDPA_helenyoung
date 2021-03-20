#   This function achieves the following learning outcomes :
#       4: Functions, Numpy, Lists
#
#Importing the functions I will need
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
#data["age"] = data["age"].astype(str)

#Converting the dataframe to a Numpy array
#data= data.to_numpy()
#print(data)
# Using Numpy Where function to create a list showing low BMI
bmi_low= np.where(data.bmi <18.5)
bmi_low_list = data.iloc[bmi_low]
#print(bmi_low_list)
# Round age
#data["Age_rounded"] = data.age.apply(np.ceil)
#print(data)

data_array= data[["gender", "age", "bmi"]].to_numpy()
print(data_array)

















