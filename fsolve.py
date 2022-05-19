from scipy.optimize import fsolve

def f(x):
    return x ** 3 - 2 * x ** 2

x = fsolve(f, x0=[1.6])

print("Root x is approx. x={}.".format(x))
print("The error is less than 1e-6")
print("The exact error is {}.".format(2 - x[0]))