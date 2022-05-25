from sympy import limit, sin, oo

print(limit(1/x, x, 50))        # what is 1/x if x --> 50
print(limit(1/x, x, oo))        # oo is infinity
print(limit(sin(x) / x, x, 0))
print(limit(sin(x) / x**2, x, 0))   # does not work

