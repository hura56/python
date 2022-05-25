import pylab as plb
import numpy as np

t = np.arange(0, 10*np.pi, 0.01)
y = np.cos(t)

plb.plot(t, y)
plb.xlabel('t')
plb.ylabel('y(t)')
plb.show()
