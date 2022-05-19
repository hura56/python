import matplotlib.pyplot as plt
import numpy as np

"""czcionke mozna ustawic globalnie za pomoca
matplotlib(lub plt).rcParams.update({'font.size':18,
 'font.family': 'serif')}"""

plt.rcParams.update({'font.size':18,
 'font.family': 'serif'})

x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()

ax.plot(x, x**2, label = r"$y = \alpha^2$")
ax.plot(x, x**3, label = r"$y = \alpha^3$")
ax.legend(loc=2) #upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('jakis tytul tako')

plt.show()