import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('kina4.xlsx')
print(df.head)
dfRok = df.groupby("Rok")
print(dfRok.mean())

dfG = df.groupby("Gestor")
dfG = dfG.mean()

plt.bar(x=dfG.index, height=dfG["Wartosc"], label="164382")
plt.legend(loc=1)
plt.savefig("Wykres.png")
plt.show()
