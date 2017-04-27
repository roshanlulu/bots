# Python file to read in the csv data

import pandas as pd


data = pd.read_csv('./data.csv')
print(data.head())
print(data.shape)
# print(data.columns)
# print(data.Date.value_counts())