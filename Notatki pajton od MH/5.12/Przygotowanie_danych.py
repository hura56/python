import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
random.seed(500)
random_names = [names[random.randint(0, len(names)-1)] for i in range(1000)]
print(random_names[:10])
births = [random.randint(0, 1000) for u in range(1000)]
print(births[:10])
BabyDataSet = list(zip(random_names, births))
print(BabyDataSet[:10])
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print(df[:10])
df.to_csv('births1880.txt', index=False, header=False)

# Wczytywanie danych

Location = './births1880.txt'
# df = pd.read_csv(Location, header=None)
df = pd.read_csv(Location, names=['Names', 'Births'])
df.info()  # informacje o danych
df.head()  # kilka pierwszych rekordów
# df.head(5)
df.tail()  # kilka ostatnich rekordów
df.tail(6)

# Analiza danych

# Trzy wersje wydobycia unikalnych imion:

print(df['Names'].unique())
for x in df['Names'].unique():
    print(x)
print(df['Names'].describe())

# Tworzymy obiekt grupowania względem imion:
name = df.groupby('Names')
print(name.head())  # te same dane inny obiekt:
print(name)
# Sumujemy względem imion:
dfsum = name.sum()
print(dfsum)

print("Separator \n")

# Modelowanie danych                            """Nie dziala"""

# Chcemy znaleźć najpopularniejsze imię.
Sorted = dfsum.sort_values(['Births'], ascending=False)
Sorted.head(1)
# Chcemy wydobyć informacje o Bobie:
df.query('(Names == "Bob" )')
df.query('(Names == "Bob" ) & (Births > 500)')
# Chcemy sprawdzić w których wierszach jest imię rozpoczynające się na 'B':
df['Names'].map(lambda x: x.startswith('B'))


# Wizualizacja

# Wykres
dfsum.plot(kind='bar')
plt.show()
# Informacje
print('Popularne imiona')
dfsum.sort_values(['Births'], ascending=False)

# Zapisanie danych

# Zapisanie danych posortowanych
Sorted.to_csv("sorted.csv")
# Zapisanie wykresu
dfsum.plot(kind='bar')
plt.savefig("wykres.pdf")
plt.savefig("wykres.png")
plt.savefig("wykres.eps")
