def f(x):
    return x

def bisect(f, a, b, ftol=1e-6):
    x = (a+b)/2.0
    while abs(f(x)) > ftol:
        if f(x)*f(a)>0:
            a = x
        else:
            b = x
        x = (a+b)/2.0
    return x

print("Root = ", bisect(f, -1.0, 2.0))