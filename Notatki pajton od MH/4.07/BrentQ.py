from scipy.optimize import brentq


def f(x):
    """returns f(x)=x^3-2x^2. Has roots at
    x=0 (double root) and x=2"""
    return x ** 3 - 2 * x ** 2


# main program starts here
x = brentq(f, a=1.5, b=3.0, xtol=1e-6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))

"""
Checking how to use BrentQ without internet:
    >Python Console
import scipy.optimize
help(scipy.optimize.brentq)
"""
