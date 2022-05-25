import sympy

x = sympy.Symbol('x')   # define symbolic
y = sympy.Symbol('y')   # variables
print(x + x)
t = (x + y) ** 2
print(t)
print(sympy.expand(t))
print(sympy.pprint(t))     # PrettyPRINT
print(sympy.printing.latex(t))

print("\nSeparator\n")

print(t)
print(t.subs(x, 3))     # substituting variables or values
print(t.subs(x, 3).subs(y, 1))
n = t.subs(x, 3).subs(y, sympy.pi)
print(n)
print(n.evalf())        # EVALuate to Float
