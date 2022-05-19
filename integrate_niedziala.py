from sympy import integrate
a, b = sympy.symbols('a, b')
print(integrate(2*x, (x, a, b)))
