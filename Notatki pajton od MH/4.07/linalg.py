import numpy.linalg as la
import numpy as np

a = np.arange(4)
a.shape = (2, 2)
print("a =", a)
ainv = la.pinv(a)
print("ainv =", ainv)
print("a*ainv = ", a.dot(ainv))
print("det(a) =", la.det(a))
print("det(ainv =", la.det(ainv))
print("det(a)*det(ainv) =", la.det(a)*la.det(ainv))
print("eigensystem(a) =", la.eig(a))

A = np.array([[1, 0], [0, 2]])
b = np.array([1, 4])
x = la.solve(A, b)
print("x =", x)

print(np.dot(A, x))
