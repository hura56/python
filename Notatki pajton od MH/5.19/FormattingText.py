from pylab import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r'$y = \alpha^2$')
ax.plot(x, x**3, label=r'$y = \alpha^3$')
ax.legend(loc=2)
ax.set_xlabel(r'$x\alpha$', fontsize=18)
ax.set_ylabel(r'$y\alpha$', fontsize=18)
ax.set_title('title')
show()
