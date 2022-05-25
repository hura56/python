from pylab import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))
# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)
# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
show()
