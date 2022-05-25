import numpy as np
from scipy.integrate import odeint
import pylab
import math


def f(y, t):
    return -0.01 * y + \
        math.sin(10 * math.pi * t)


ts = np.arange(0, 2.01, 0.01)
y0 = -2
ys = odeint(f, y0, ts)

pylab.plot(ts, ys, 'g')
pylab.savefig('odeintexample2.pdf')
pylab.show()
