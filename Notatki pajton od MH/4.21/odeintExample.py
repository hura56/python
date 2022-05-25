import numpy as np
from scipy.integrate import odeint
import pylab


def f(y, t):
    return -2 * y


ts = np.arange(0, 2.1, 0.1)
y0 = 17
ys = odeint(f, y0, ts)

pylab.plot(ts, ys, 'x')
pylab.grid()
pylab.savefig('odeintexample1.pdf')
pylab.show()
