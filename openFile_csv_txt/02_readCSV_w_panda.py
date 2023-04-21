import pandas as pd
cutmrs = pd.read_csv('customers.csv')     # Import the file '.csv' as Arry Fileds.
print(cutmrs)
#      CustomerID    FirstName      LastName         City State
# 0          6192        Randi    Piedrahita  Canoga Park    CA
# 1       5100595  Christopher       Abraham   Loma Linda    CA
# 2       1902451        Elvis      Jauregui  Los Angeles    CA
# ..          ...          ...           ...          ...   ...
# 600     5415481         John        Hughes    Round Top    TX
# 601     5415482      Phillip        Okonma  Los Angeles    CA

print(cutmrs['CustomerID'])
# 0         6192
# 1      5100595
# 2      1902451
#         ...   
# 601    5415482

print(cutmrs['CustomerID'][0])