from scipy.optimize import newton

"""
The newton method has much better convergence than the bisection method,
however, it is not guaranteed to converge.
Needs a good initial guess x for the root.
"""


def f(x):
    """returns f(x)=x^3-2x^2. Has roots at
    x=0 (double root) and x=2"""
    return x ** 3 - 2 * x ** 2


# main program starts here
x = newton(f, x0=1.6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))
