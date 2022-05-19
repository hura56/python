import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) #pozycja x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

xx = np.linspace(-0.75,1.,100)
ax.plot(xx, xx**3)


plt.show()