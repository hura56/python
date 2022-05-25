from numpy import array, arange
from scipy.integrate import odeint
import pylab


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
y0 = array([r0, v0])

ys = odeint(f, y0, ts)

rs = ys[:, 0]
vs = ys[:, 1]


pylab.plot(ts, rs, 'b', label='r(t)')
pylab.plot(ts, vs, 'g', label='v(t)')
pylab.legend()
pylab.savefig('2ndOrderODE.pdf')
pylab.show()
