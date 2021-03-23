#   This function achieves the following learning outcomes :
#       5. Seaborn, Matplotlib


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
#print(request.status_code)

# Import CSV file from Kaggle.
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")

# To round Age in the dataset.
data["age"] = data["age"].apply(lambda x :round(x))

# To eliminate outliers in dataset.
data["bmi"] = data["bmi"].apply(lambda bmi_value: bmi_value if 12 < bmi_value < 60 else np.nan)

# Elimination of null values in BMI using forward fill method.
data['bmi'].ffill(inplace= True)

# Dropped ID as not required.
data= data.drop(["id"], axis=1)
#print(data.isnull().sum())

# To remove 1 line as "Other" in Gender.
lines_drop= data[data["gender"] =="Other"].index
data.drop(lines_drop,inplace=True)

# Creating a dataset with details for stoke only.
data_stroke = data[data["stroke"]==1]

# Histogram to find correlation between age, BMI and incidence of stroke
plt.figure(figsize=(8,8))
ax = sns.scatterplot(x="bmi", y="age", alpha= 0.5, data=data[data["stroke"]==0])
sns.scatterplot(x="bmi", y="age", alpha= 1, data=data[data["stroke"]==1], ax=ax)
# # plt.show()

# Bar Chart to show Incidence of Stoke based on gender.
plt.figure(figsize=(8,8))
plt.title("Incidence of Stoke based on Gender")
sns.countplot(x=data_stroke["stroke"], hue= data["gender"])
plt.xlabel("Gender")
plt.ylabel("Count")
# plt.show()

# Bar Chart to show Incidence of Stoke based on Employment type.
plt.figure(figsize=(8,8))
plt.title("Incidence of Stoke based on Employment Type")
sns.countplot(x=data_stroke["stroke"], hue= data["work_type"])
plt.xlabel("Employment Type")
plt.ylabel("Count")
# plt.show()

# Bar Chart to show Incidence of Stoke based on Relationship status.
plt.figure(figsize=(8,8))
plt.title("Incidence of Stoke based on Relationship Status")
sns.countplot(x=data_stroke["stroke"], hue= data["ever_married"])
plt.xlabel("Relationship Status")
plt.ylabel("Count")
# plt.show()

# Bar Chart to show Incidence of Stoke based on Residence Type.
plt.figure(figsize=(8,8))
plt.title("Incidence of Stoke based on Residence Type")
sns.countplot(x=data_stroke["stroke"], hue= data["Residence_type"])
plt.xlabel("Residence Type")
plt.ylabel("Count")
plt.show()






