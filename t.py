a=(10,20,30)
print(type(a))
print(a[1])
print(a[0])
print(a[:-1])
x=1
y=2
print(x,y)
x,y=y,x
print(x,y)
def f(x):
    return x**2, x**3
i,j=f(2)
print(i,j)