import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots(figsize=(6,2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
#usuniecie z prawej strony
ax.spines['right'].set_color('none')
ax.yaxis.tick_left() #tylko ticks po lewej stronie

plt.show()