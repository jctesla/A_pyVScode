import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df = df.reset_index()
print(df, "\n")

#   index  A  B
# 0     a  1  4
# 1     b  2  5
# 2     c  3  6


# ------------ Build cars DataFrame -----------------------------
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

cars_dict = { 'country':names, 'drivers':dr, 'cars_percap':cpc }

cars = pd.DataFrame(cars_dict)
print(cars)

#          country  drives   cars_percap
# 0  United States    True           809
# 1      Australia    False          731
# 2          Japan    False          588
# 3          India    False           18
# 4         Russia    True           200
# 5        Morocco    True            70
# 6          Egypt    True            45



# To Change de valies index of 0,1,2,3,4,5,6 by labels:
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']  # Definition of row_labels
cars.index =row_labels                                      # Specify row labels of cars
print(cars)
#            country  drives_right  cars_per_cap
# US   United States          True           809
# AUS      Australia         False           731
# JPN          Japan         False           588
# IN           India         False            18
# RU          Russia          True           200
# MOR        Morocco          True            70
# EG           Egypt          True            45

print(cars['country'])
# US     United States
# AUS        Australia
# JPN            Japan
# IN             India
# RU            Russia
# MOR          Morocco
# EG             Egypt

print(cars['country']['US'])              # Name: 'country', dtype: object: 'United States'
cars['country']['US'] = 'Estados Unidos'  # change value

print(cars['country'])
# US     Estados Unidos
# AUS         Australia
# JPN             Japan
# IN              India
# RU             Russia
# MOR           Morocco
# EG              Egypt