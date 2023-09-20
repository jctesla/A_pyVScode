# se puede usar para recopilar datosd e un circuito datalogger  en .csv y leerlo con pandas.
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']    # build body : DataFrame
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc }
cars = pd.DataFrame(my_dict)                                              # build titles : DataFrame

print(cars)                                                               # index automatic created
#          country  drives_right  cars_per_cap
# 0  United States          True           809
# 1      Australia         False           731
# 2          Japan         False           588
# 3          India         False            18
# 4         Russia          True           200
# 5        Morocco          True            70
# 6          Egypt          True            45