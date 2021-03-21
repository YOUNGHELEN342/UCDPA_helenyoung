#   This function achieves the following learning outcomes :
#       2. Importing data
#       3. Analysing data

#Importing the functions I will need
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json

print(os.getcwd())

# API from Kaggle and checking successful import.
request=requests.get("https://www.kaggle.com/fedesoriano/stroke-prediction-dataset")
print(request.status_code)

# Import CSV file from Kaggle.
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")

# To see what the dataset looks like.
print(data)
print(data.info())
print(data.isnull().sum()) #Can see null values in BMI

# To round Age in the dataset.
data["age"] = data["age"].apply(lambda x :round(x))

# To eliminate outliers in dataset.
data["bmi"] = data["bmi"].apply(lambda bmi_value: bmi_value if 12 < bmi_value < 60 else np.nan)

# Elimination of null values in BMI using forward fill method.
data['bmi'].ffill(inplace= True)

# Dropped ID as not required.
data= data.drop(["id"], axis=1)
print(data.isnull().sum())

# To remove 1 line as "Other" in Gender.
lines_drop= data[data["gender"] =="Other"].index
data.drop(lines_drop,inplace=True)

# To show there are no null values remaining.
print(data.isnull().sum())

# Sort dataset by gender & age
data.sort_values(["gender", "age"], inplace = True)
data.reset_index(drop=True, inplace = True)

# Sorting BMI in desending order and saving as data_sorted
data_sorted = data.sort_values("bmi", False)

# Grouping the dataset by gender and saving as data_group-Noticed there was 1 line as "Other"
data_group = data.groupby("gender").count()
print(data_group)
#
# Data on females only from columns gender to age.
data_female= data.loc[data.gender == "Female", "gender": "age"]

# Socio-economic data only ie: Marriage status, Employment type & Residence type for all genders.
data_social = data.iloc[:,4:7]

# To merge data_social & data_female.
df_cat = pd.concat([data_social, data_female], axis=1)

# To fill null values in merged datasets.
df_cat.fillna(value=0, inplace= True)
print(df_cat)
#
# Use iterrows to add uppercase column "Gender" to data_social
for lab, row in data.iterrows():
    data_social.loc[lab, "GENDER"] = row["gender"].upper()

print(data_social)




















































