import numpy as np
from scipy.integrate import odeint
import pylab


def rhs(y, t):
    a = 0.7
    b = 1
    c = 0.007
    p1 = y[0]
    p2 = y[1]
    dp1dt = a * p1 - c * p1 * p2
    dp2dt = c * p1 * p2 - b * p2
    return np.array([dp1dt, dp2dt])


p0 = np.array([70, 50])     # initial condition
ts = np.arange(0, 30, 0.1)

res = odeint(rhs, p0, ts)       # compute solution

print(res)

p1 = res[:, 0]      # extract p1 and
p2 = res[:, 1]      # p2

pylab.plot(ts, p1, label='rabbits')
pylab.plot(ts, p2, '-og', label='foxes')
pylab.legend()
pylab.xlabel('t')
pylab.savefig('predprey.eps')
pylab.savefig('pregprey.png')
pylab.show()
