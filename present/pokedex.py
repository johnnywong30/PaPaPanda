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
    english_dex.loc[row + 1] = [name, type, int(stats['HP']), int(stats['Attack']), int(stats['Defense']), int(stats['Sp. Attack']), int(stats['Sp. Defense']), int(stats['Speed'])]
    #print(english_dex)
#print(english_dex)

pangoro = english_dex[english_dex.Name == 'Pangoro']
#pangoro.plot.bar(x='Name')
#print(pangoro)

alakazam = english_dex[english_dex.Name == 'Alakazam']
#alakazam.plot.bar(x='Name')
#print(alakazam)

# create a new DataFrame after adding rows of n number of DataFrames together
duel = pd.concat([pangoro, alakazam])
#duel.plot.barh(x='Name')
#print(duel)
#plt.show()

# Dex nums to play around with by region
# Kanto:    001 - 151
# Johto:    152 - 251
# Hoenn:    252 - 386
# Sinnoh:   387 - 493
# Unova:    494 - 649
# Kalos:    650 - 721
# Alola:    722 - 809

# Kanto dex
kanto = english_dex.loc[0:151]
#print(kanto)
attack_kanto = pd.DataFrame(columns=['Name', 'Type', 'Attack', 'Speed'])
for (row, series) in kanto.iterrows():
    name = series['Name']
    type = series['Type']
    attack = int(series['Attack'])
    speed = int(series['Speed'])
    attack_kanto.loc[row] = [name, type, attack, speed]

attack_kanto.plot.line(x='Name')

# get the row with the highest attack
print(attack_kanto.loc[attack_kanto['Attack'].astype(int).idxmax()])

# get the row with the highest speed
print(attack_kanto.loc[attack_kanto['Speed'].astype(int).idxmax()])
plt.show()
