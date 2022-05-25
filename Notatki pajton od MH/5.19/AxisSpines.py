from pylab import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots(figsize=(6, 2))
ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
ax.yaxis.tick_left()  # only ticks on the left side
show()
