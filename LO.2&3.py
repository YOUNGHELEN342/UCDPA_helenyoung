#   This function achieves the following learning outcomes :
#       2. Importing data
#       3. Analysing data

import os

import pandas as pd
import numpy as py
print(os.getcwd())
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")
data= data.drop(["id"], axis=1)
print(data.isnull().sum())
data= data.dropna(subset=['bmi'], axis=0)
print(data.isnull().sum())
print(data.shape)
data["age"] = pd.to_numeric(data["age"], errors="coerce")
data.sort_values("age")
print(data)


































