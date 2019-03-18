# PaPaPandas - Jack Lu & Johnny Wong
# SoftDev2 pd8
# 2019-03-18

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

try:
    os.remove('./a.csv')
except:
    pass

def format(code):
    print()
    print('=' * 50)
    print('| ' + code + ' |')


# Data structures
# series
format('s = pd.Series(np.random.randn(10))')
s = pd.Series(np.random.randn(10))
print(s)


#dataframe
format("df = pd.read_csv('data.csv')")
df = pd.read_csv('data.csv')
print(df)

format('dtypes')
print(df.dtypes)

format('index')
print(df.index)

format('columns')
print(df.columns)

format('values')
print(df.values)

format('describe')
print(df.describe())

format('sorting by gpa column')
print("df.sort_values('gpa', ascending=False)")
print(df.sort_values('gpa', ascending=False))

format('get a single column - print(df.iq)')
print(df.iq)

format('get multiple columns - print(df[["name"]["gpa"]])')
print(df[['name', 'gpa']])
# Retrieving data

format('df.loc - get all cells from specified rows and columns')
print(df.loc[2:3, ['name', 'iq']])

format('inserting a new column')
print("df['gpa_4.0'] = df.gpa / 25")
df['gpa_4.0'] = df.gpa / 25
print(df)

format('renaming columns')
print("df.columns = [0,1,2,3,4]")
df.columns = [0,1,2,3,4]
print(df)

format('converting dataframe to file')
print("df.to_csv('a.csv')")
#df.to_csv('a.csv')
