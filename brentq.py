from scipy.optimize import brentq

def f(x):
    return x ** 3 - 2 * x ** 2

x = brentq(f, a=1.5, b=3, xtol=1e-6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6")
print("The exact error is {}.".format(2 - x))