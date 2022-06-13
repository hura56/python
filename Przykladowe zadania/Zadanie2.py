import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

df = pd.read_excel('ceny3.xlsx')

x1 = df["Rok"]
y1 = df["Wartość"]

plt.plot(x1, y1, ls='-', color="blue", label="Ceny w danym roku")
plt.legend(loc='upper right')
plt.title("Ceny ryż - za 1kg w ciągu lat w zł")
plt.annotate(xy=[2018.7, 3.77], text="10.06.2022")

plt.xlabel("Rok")
plt.ylabel("Cena")

plt.grid()
plt.savefig("Zadanie2.pdf")
plt.show()

