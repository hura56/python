import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
fig, ax = plt.subplots()

ax.plot(x, x**2, 'b.-') #niebieski z kropkami
ax.plot(x, x**3, 'g.-') #zielony z kropkami
ax.legend(loc=2) #upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('jakis tytul tako')

plt.show()