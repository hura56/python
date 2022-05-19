from math import cos, exp, pi
from scipy.integrate import quad

def f(x):
    return exp(cos(-2 * x * pi)) +3.2

res, err=quad(f, -2, 2)

print("Wynik {:f} (+-{:g})".format(res,err))