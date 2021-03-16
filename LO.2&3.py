#   This function achieves the following learning outcomes :
#       2. Importing data
#       3. Analysing data

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



print(os.getcwd())
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")
data= data.drop(["id"], axis=1)
# Dropped ID as don't need it
print(data.isnull().sum())
data= data.dropna(subset=['bmi'], axis=0)
# Got rid of the null values that I saw in BMI
lines_drop= data[data["gender"] =="Other"].index
data.drop(lines_drop,inplace=True)
#To remove 1 line as "Other"
print(data.isnull().sum())
print(data.shape)
print(data.columns)
data_sorted = data.sort_values("bmi", False)
# Sorting BMI in desending order and saving as data_sorted
data_group = data.groupby("gender").count()
# Grouping the dataset by gender and saving as data_group-Noticed there was 1 line as "Other"
print(data_group)
print(data)

data_female= data.loc[data.gender == "Female", "age": "bmi"]


data_social = data.iloc[:,4:7]
print(data_social)








































