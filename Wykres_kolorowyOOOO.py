import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
fig, ax = plt.subplots()

ax.plot(x, x+1, color='red', alpha=0.5) #alpha 0.5 to półprzezroczystość
ax.plot(x, x+2, color='#1155dd')
ax.plot(x, x+3, color='#15cc55')
ax.legend(loc=2) #upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('jakis tytul tako')

plt.show()