import numpy as np
from scipy.integrate import odeint
def f(y,t):
    return -2 * y

ts = np.arange(0, 2.1, 0.1)
y0 = 17
ys = odeint(f, y0, ts)

import pylab
pylab.plot(ts, ys, 'x')
pylab.grid(); pylab.savefig('odeintexample.pdf')
pylab.show()
