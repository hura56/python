from pylab import *
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots()

ax.plot(x, x**2, 'b.-', label=r'$y = \alpha^2$')    # Blue line with dots
ax.plot(x, x**3, 'g--', label=r'$y = \alpha^3$')    # Green dashed line
ax.legend(loc=2)
ax.set_xlabel(r'$x\alpha$')
ax.set_ylabel(r'$y\alpha$')
ax.set_title('title')
show()


fig2, ax = plt.subplots()

ax.plot(x, x+1, color="red", alpha=0.5)  # half-transparant red
ax.plot(x, x+2, color="#1155dd")  # RGB hex code for a bluish color
ax.plot(x, x+3, color="#15cc55")  # RGB hex code for a greenish color
ax.set_xlabel(r'$x\alpha$')
ax.set_ylabel(r'$y\alpha$')
ax.set_title('title')
show()
