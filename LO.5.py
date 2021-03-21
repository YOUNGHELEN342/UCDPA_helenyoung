#   This function achieves the following learning outcomes :
#       5. Seaborn, Matplotlib
#

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

# To see what the dataset looks like.
#print(data)
#print(data.info())
#print(data.isnull().sum()) #Can see null values in BMI

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
print(data_stroke)

# x= data_stroke["age"]
# y= data_stroke[""]
# plt.plot(x,y)
# plt.show()

# sns.countplot(x='gender', hue="stroke", data=data_stroke)
# plt.show()

# To find correlation between age, BMI and incidence of stroke
plt.figure(figsize=(8,8))
ax = sns.scatterplot(x="bmi", y="age", alpha= 0.5, data=data[data["stroke"]==0])
sns.scatterplot(x="bmi", y="age", alpha= 1, data=data[data["stroke"]==1], ax=ax)

# sns.countplot(x='smoking_status', hue="stroke", data=data_stroke)
# plt.show()

data_stroke.groupby(["stroke"]).work_type.value_counts().plot.bar()

data_stroke.groupby(["stroke"]).smoking_status.value_counts().plot.bar()
plt.show()













