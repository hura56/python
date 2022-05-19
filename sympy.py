import sympy
x = sympy.Symbol('x')
y = sympy.Symbol('y')
x + x
2*x
t = (x+y)**2
print(t)
(x+y)**2
print(sympy.expand(t))
sympy.pprint(t)
print(t.subs(x,3))
n = t.subs(x,3), t.subs(y,sympy.pi)
print(n)
# print(n.evalf()) ?
p = sympy.pi
print(p)

