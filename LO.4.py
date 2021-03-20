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

# Using Numpy Where function to create a list showing low BMI *****USING THIS*****
#bmi_low= np.where(data.bmi <18.5)
#bmi_low_list = data.iloc[bmi_low]
#print(bmi_low_list)
# Round age *****PROB WILL NOT USE THIS****
#data["Age_rounded"] = data.age.apply(np.ceil)
#print(data)


#data_list= data["bmi"].to_list()
#print(data_list)
#Converting data_female to a list *****WILL USE THIS****
#data_female= data.loc[data.gender == "Female", "gender": "age"]
#print(data_female.values.tolist())

data_female= data.loc[data.gender == "Female", "gender": "age"]
data_array= data.to_numpy()
print(data_array)


















