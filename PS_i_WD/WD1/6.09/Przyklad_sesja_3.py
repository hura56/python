import pylab as plt
import numpy as np
import pandas as pd

df = pd.read_csv("sprzedaz4.csv", sep="@")

df = df.T

df = df.reset_index()
df.columns = ["Owoc", "Rok", "Wartosc"]

dfG = df.groupby("Rok")
dfG = dfG.sum()
print(dfG)

plt.plot(dfG.index)
plt.savefig("Wykres3.jpg")  # Unfinished
plt.show()
