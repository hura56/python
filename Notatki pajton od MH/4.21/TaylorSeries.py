from sympy import series
taylorseries = series(sin(x), x, 0)
print(taylorseries)
print(sympy.pprint(taylorseries))   # does not work
