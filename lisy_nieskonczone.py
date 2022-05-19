import numpy as np
from scipy.integrate import odeint
def rhs(y, t):
    a = 0.7
    c = 0.007
    b = 1
    p1 = y[0]
    p2 = y[1]
    dp1dt = a*p1-c*p1*p2
    dp2dt = c*p1