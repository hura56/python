import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig, ax = plt.subplots(figsize=(10,4))

ax.plot(x, x**2, x, x**3, lw=2)

ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'],
fontsize=18)

yticks = [0,50,100,150]
ax.set_yticks(yticks)
ax.set_yticklabels(['$%.1f$' % y for y in yticks], fontsize=18)

plt.show()
