
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad

csv = pd.read_csv('nieruchomosci2.csv', sep=';', header=None)
df = pd.DataFrame(csv)
df.loc[3, :] = df.loc[3, :].str.replace(" ", "").astype(int)
df = df.T

df.columns = ['rynek', 'Metraz', 'Rok', 'ilosc']
print(df)

# wybieramy jaki typ wartości nas interesuje
grupa = df.where(df['rynek'] == 'rynek wtórny')
# Czy sumujemy czy Średnia
grupa = grupa.groupby('Metraz').agg({'ilosc': 'sum'})

grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=10, figsize=(8, 8))
plt.legend(title='metraż')
plt.title('wykres przedstawiający stosunek ilości mieszkań poszczególnych metraży sprzedanych w 2 roku')
plt.show()