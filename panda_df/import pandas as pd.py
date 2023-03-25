import pandas as pd
from matplotlib import pyplot as plt

#Pandas loads out data
df = pd.read_csv(‘rason.csv’)

#Matplotlib plots and displays grafic
plt.plot(df.letter, df.frequency)
plt.show()
