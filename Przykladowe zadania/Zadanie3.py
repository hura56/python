import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

df = pd.read_csv('sport3.csv', sep=";")
df.iloc[:, 4] = pd.Series(df.iloc[:, 4], dtype=int)
df.iloc[:, 5] = pd.Series(df.iloc[:, 5], dtype=int)

data1 = df.where(df["Nazwa"] == "WARMIŃSKO-MAZURSKIE").dropna()
data2 = df.where(df["Nazwa"] == "POMORSKIE").dropna()

print(data2)

plt.bar(data1.index, data1["Wartość"], align='center', color='red')
plt.bar(data2.index, data2["Wartość"], align='center', color='purple')
plt.title("Wykres")
plt.xlabel("województwa")
plt.ylabel("wartości")

plt.legend(['Warminsko-mazurskie', 'Pomorskie'], loc=(0.5, 0.75))
plt.grid()
plt.savefig("Zadanie3.jpg")
plt.show()

print(data1)

