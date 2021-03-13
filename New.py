import os

import pandas as pd

print(os.getcwd())
data = pd.read_csv("healthcare-dataset-stroke-data.csv")
print(data.head())
print(data.tail())
print(data.shape)
print(data.isnull().sum())
data.fillna
data_filled = data.fillna(method = "ffill", axis = 0).fillna(0)
print(data_filled.isnull().sum())
data_final = data_filled.drop_duplicates(subset=["id"])
print ("Heloo")
















