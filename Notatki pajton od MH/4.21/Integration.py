from sympy import integrate
a, b = sympy.symbols('a, b')
print(integrate(2*x, (x, a, b)))
print(integrate(2*x, (x, 0.1, b)))
print(integrate(2*x, (x, 0.2, 2)))  # does not work
