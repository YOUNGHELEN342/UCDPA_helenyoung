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

# To show there are no null values remaining.
print(data.isnull().sum())
print(data.shape)
print(data.columns)

# Sorting BMI in desending order and saving as data_sorted
data_sorted = data.sort_values("bmi", False)

# Grouping the dataset by gender and saving as data_group-Noticed there was 1 line as "Other"
data_group = data.groupby("gender").count()

print(data_group)


# Data on females only from age to BMI
data_female= data.loc[data.gender == "Female", "age": "bmi"]

# Socio-economic data only ie: Marraige status, Employment type & Residence type for all genders.
data_social = data.iloc[:,4:7]
# Age for all genders
data_gender_age= data.iloc[:,0:2]

#Merge data_social & data_gender_age
df_cat = pd.concat([data_social, data_gender_age], axis=1)
print(df_cat)















































