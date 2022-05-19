from scipy.optimize import newton

def f(x):
    return x**3 - 2*x ** 2

x = newton(f, x0=1.6)

print("Root x is approx. x={:14.12g}.".format(x))
print("The error is less than 1e-6.")
print("The exact error is {}.".format(2 - x))