import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

x = [1, 2, 3, 4]

x1 = [32, 34, 30, 7]
y1 = [-14, -28, -21, -13]
#colors: https://matplotlib.org/stable/gallery/color/named_colors.html
col1 = 'yellow', 'aqua', 'purple', 'aqua'

x2 = [41, 37, 32, 41]
y2 = [38, 21, 24, 21]
col2 = 'gray', 'orange', 'red', 'pink'

fig, axs = plt.subplots(1,2)

hbar1 = axs[0].barh(x, y1, align='center', tick_label=x1, color=col1)
axs[0].set_xlim([-30, 0])
axs[0].xaxis.set_major_locator(MultipleLocator(5))
axs[0].set_title("1_2")

hbar2 = axs[1].barh(x, y2, align='center', tick_label=x2, color=col2)
axs[1].set_xlim([0, 40])
axs[1].xaxis.set_major_locator(MultipleLocator(10))
axs[1].set_title("2_2")

plt.savefig("zadani1.png")
plt.show()