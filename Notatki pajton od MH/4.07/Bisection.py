"""
How to write a bisection function:
1. x = (a+b)/2
2. while |f(x)| > ftol do:
        if f(x)f(a) > 0
        then a <- x
        else b <- x
        x = (a+b)/2
3. return x
"""


def f(x):
    return x


def bisect(f, a, b, ftol=1e-6):
    x = (a+b)/2.0
    while abs(f(x)) > ftol:
        if f(x)*f(a) > 0:
            a = x
        else:
            b = x
        x = (a+b)/2.0
    return x


print("Root =", bisect(f, -1.0, 2.0))
