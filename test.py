import pandas as pd

import numpy as np

import random


#import matplotlib.pyplot as plt

#f = open('game.csv', 'r')
#for i in f:
#    print(i)

s = pd.Series([1,3,5,np.nan,6,8])
#print(s)

#data = pd.read_csv('game.csv', delimiter = ',')
#print(data.head())

dataframe2 = pd.DataFrame({'Coolness': 1, 'Date': pd.Timestamp('20190215'), 'Hotness': np.array([random.random()] * 3, dtype='float32')})
print(dataframe2)
print(dataframe2.describe())
