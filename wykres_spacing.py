import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
fig, ax = plt.subplots(1, 1)

ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0,50,100,150])

ax.set_title('label and axis spacing')

ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5

ax.set_xlabel('x')
ax.set_ylabel('y')


plt.show()