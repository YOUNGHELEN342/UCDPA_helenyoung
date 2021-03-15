#   This function achieves the following learning outcomes :
#       2. Importing data
#       3. Analysing data

import os
import pandas as pd
import numpy as np


print(os.getcwd())
data = pd.read_csv("Data Files\\healthcare-dataset-stroke-data.csv")
data= data.drop(["id"], axis=1)
print(data.isnull().sum())
data= data.dropna(subset=['bmi'], axis=0)
print(data.isnull().sum())
print(data.shape)
data_sorted = data.sort_values("bmi", False)

data_group = data.groupby("gender").count() 
print(data_group)





































