# PaPaPandas - Jack Lu & Johnny Wong
# SoftDev2 pd8
# 2019-03-18

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pokedex presentation

# pokedex is a dataframe built from the pokedex.json that is read
pokedex = pd.read_json('pokedex.json')

# showcase DataFrame
#print(pokedex)

# create a more organized DataFrame
english_dex = pd.DataFrame(columns=['Name', 'Type', 'HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed'])

# dataframe.iterrows() iterates over the DataFrame as (index, Series) pairs
# similar to a dictionary with (key, value)
for (row, series) in pokedex.iterrows():
    # access the english name in name Series of the original pokedex DataFrame
    name = series['name']['english']
    # access the dictionary of base stats in the base Series of the original pokedex DataFrame
    stats = series['base']
    # set each row to corresponding data in each column for the new DataFrame
    type = series['type']
    english_dex.loc[row + 1] = [name, type, stats['HP'], stats['Attack'], stats['Defense'], stats['Sp. Attack'], stats['Sp. Defense'], stats['Speed']]
print(english_dex)

pangoro = english_dex[english_dex.Name == 'Pangoro']
#pangoro.plot.bar(x='Name')
print(pangoro)

alakazam = english_dex[english_dex.Name == 'Alakazam']
#alakazam.plot.bar(x='Name')
print(alakazam)

# create a new DataFrame after adding rows of n number of DataFrames together
duel = pd.concat([pangoro, alakazam])
duel.plot.bar(x='Name')
print(duel)
plt.show()
