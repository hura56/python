from pylab import *
from matplotlib import ticker
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, x**2, x, x**3, lw=2)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)
yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18)  # use LaTeX formatted labels
show()

# Scientific notation

fig2, ax = plt.subplots(1, 1)
ax.plot(x, x**2, x, np.exp(x))
ax.set_title("scientific notation")
ax.set_yticks([0, 50, 100, 150])
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))
ax.yaxis.set_major_formatter(formatter)
show()
