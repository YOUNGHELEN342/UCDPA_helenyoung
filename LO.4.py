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

#print(data.isnull().sum())

# Elimination of null values that I saw in BMI.
data= data.dropna(subset=['bmi'], axis=0)

#To remove 1 line as "Other" in Gender.
lines_drop= data[data["gender"] =="Other"].index
data.drop(lines_drop,inplace=True)

# Converting the dataframe to a Numpy array
# data= data.to_numpy()
# print(data)

# # Using Numpy "Where" function to create a list showing low BMI
# bmi_low= np.where(data.bmi <18.5)
# bmi_low_list = data.iloc[bmi_low]
#print(bmi_low_list)

data_max= data.loc[:, "age":"bmi"].apply(max,axis=0)
print(data_max)



# Using dictionaries to convert the different categories in the dataset to numerical data.
# gender_dict = {"Male": 0, "Female": 1}
# relationship_dict = {"No" :0, "Yes":1}
# smoking_history_dict = {"Unknown" :0, "smokes":1, "never smoked":2, "formerly smoked": 3}
# residence_type_dict = {"Urban": 0, "Rural" :1}
#
# data["gender"] = data["gender"].map(gender_dict)
# data["ever_married"] = data["ever_married"].map(relationship_dict)
# data["smoking_status"] = data["smoking_status"].map(smoking_history_dict)
# data["Residence_type"] = data["Residence_type"].map(residence_type_dict)
#print(data)


# #Converting dataframe columns "Age" and "Residence type to lists & using functions to manipulate the content
# residence_list = data["Residence_type"].to_list()
# print(residence_list.count("Urban"))
#
# age_list = data["age"].to_list()
# age_list.sort()
# print(age_list)
#























