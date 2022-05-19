import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color='blue', linewidth=0.25)
ax.plot(x, x+2, color='blue', linewidth=0.50)
ax.plot(x, x+3, color='blue', linewidth=1.00)
ax.plot(x, x+4, color='blue', linewidth=2.00)
ax.plot(x, x+5, color='red', lw=2, linestyle='-')
ax.plot(x, x+6, color='red', lw=2, ls='-.')
ax.plot(x, x+7, color='orange', lw=2, ls=':')
line, = ax.plot(x, x+8, color='black', lw=1.50)
line.set_dashes([5,10,15,10])
ax.plot(x, x+9, color='green', lw=0.5, ls='--', marker='+')
ax.plot(x, x+10, color='green', lw=0.5, ls='--', marker='o')
ax.plot(x, x+11, color='green', lw=0.5, ls='--', marker='s')
ax.plot(x, x+12, color='green', lw=0.5, ls='--', marker='1')
ax.plot(x, x+13, color='purple', lw=1, ls='-', marker='o',
markersize=2)

ax.plot(x, x+14, color='purple', lw=1, ls='-', marker='o',
markersize=4)

ax.plot(x, x+15, color='purple', lw=1, ls='-', marker='o',
markersize=8, markerfacecolor='red')

ax.plot(x, x+16, color='purple', lw=1, ls='-', marker='s',
markersize=8, markerfacecolor='yellow', markeredgewidth=2,
markeredgecolor='blue')


ax.legend(loc=2) #upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('jakis tytul tako')

plt.show()