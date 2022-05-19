from numpy import array, arange
from scipy.integrate import odeint
def f(y, t):
    omega = 1
    r = y[0]
    v = y[1]
    drdt = v
    dvdt = -omega ** 2 * r
    return array([drdt, dvdt])
ts = arange(0, 20, 0.1)
r0 = 1
v0 = 0
y0 = array([r0,v0])
ys = odeint(f, y0, ts)
rs = ys[:,0]
vs = ys[:,1]

import pylab
pylab.plot(ts, rs, label='r(t)')
pylab.plot(ts, vs, label='v(t)')
pylab.grid(); pylab.savefig('wykresy.pdf')
pylab.show()