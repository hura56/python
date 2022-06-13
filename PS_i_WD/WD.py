import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d

# ZADANIE 1
# x = [1,2,3,4,5]
#
# x1 = [5,2,6,5,4]
# y1 = [54,22,83,89,80]
# #colors: https://matplotlib.org/stable/gallery/color/named_colors.html
# col1 = 'indigo', 'aquamarine', 'orange', 'coral', 'lime'
#
# x2 = [1, 4, 6, 8, 8]
# y2 = [-53, -83, -77, -14, -76]
# #colors: https://matplotlib.org/stable/gallery/color/named_colors.html
# col2 = 'pink', 'orangered', 'hotpink', 'slategrey', 'blue'
#
# fig, axs = plt.subplots(1,2)
#
# hbar1 = axs[0].barh(x, y1, align='center', tick_label=x1, color = col1)
# axs[0].set_xlim([0,100])
# axs[0].bar_label(hbar1, y1, fmt='%.2f', padding=2)
# axs[0].set_title("Tytul 1")
#
# hbar2 = axs[1].barh(x, y2, align='center', tick_label=x2, color = col2)
# axs[1].set_xlim([-100, 0])
# axs[1].bar_label(hbar2, y2, fmt='%.2f', padding=2)
# axs[1].set_title("Tytul 2")
#
# plt.show()

# ZADANIE 2
# df = pd.read_excel('ceny2.xlsx')
#
# srednia = df.groupby("Rodzaje towarów").mean()
# srednia = srednia.reset_index()
#
# data1 = df.where(df["Rodzaje towarów"] == "ryż - za 1kg").dropna()
# data2 = df.where(df["Rodzaje towarów"] == "mąka pszenna - za 1kg").dropna()
#
# x1 = data1["Rok"]
# y1 = data1["Wartość"]
#
# x2 = data2["Rok"]
# y2 = data2["Wartość"]
#
# print(srednia)
#
# plt.plot(x1, y1, ls='-', color="red", label="ryż - za 1kg")
# plt.plot(x2, y2, ls=':', c="blue", label = "mąka pszenna - za 1kg")
# plt.legend(loc='center')
# plt.title("Wykres")
# plt.annotate(xy=[2009.7, 1.85], text="numer indeksu")
#
# plt.savefig("Zadanie2.jpg")
# plt.show()

# ZADANIE 3
# df = pd.read_csv('nieruchomosci2.csv', sep=";")
# df = df.T.reset_index()
# df.columns = ["Rynek", "Metry", "Rok", "Cena"]
#
# y1 = [14,24,17,24,21]
# lab1 = 'A', 'B', 'C', 'D', 'E'
# #colors: https://matplotlib.org/stable/gallery/color/named_colors.html
# col1 = 'indigo', 'aquamarine', 'orange', 'coral', 'lime'
# explode1 = (0.1, 0, 0, 0, 0)
#
# y2 = [74,94,83,38,76]
# lab2 = 74,94,83,38,76
# #colors: https://matplotlib.org/stable/gallery/color/named_colors.html
# col2 = 'pink', 'orangered', 'hotpink', 'slategrey', 'blue'
# explode2 = (0.1, 0, 0, 0, 0)
#
# fig, axs = plt.subplots(2,1)
#
# axs[0].pie(y1, colors = col1, labels= lab1, explode = explode1, autopct='%1.0f%%', labeldistance=1.2, shadow=True)
# # axs[0].pie(y1, colors = col1, labels= lab1, explode = explode1, autopct='%1.0f%%', labeldistance=1.2)
# axs[0].set_title("Tytul 1")
#
# axs[1].pie(y2, colors = col2, labels=lab2, explode = explode2, labeldistance=1.2)
# axs[1].set_title("Tytul 2")
# axs[1].legend(lab1, loc=(-1.0, 0.0))
#
# plt.savefig("plot.png", dpi=200)
# plt.show()
