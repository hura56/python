import numpy as np

a = np.array([1, 4, 10])
print(a)

B = np.array([[0, 1.5], [10, 12]])
print(B)
print(B.shape)

B.shape = (4, )

print(B)
print(B.shape)

print("Separator po B")

print(a.size)
print(B.size)

print(a.nbytes)
print(B.nbytes)

print(a.dtype)
print(B.dtype)

print("Separator po rozmiarach")

a2 = np.array([1, 4, 10], float)
print(a2)
print(a2.dtype)

print(np.zeros((3, 3)))
print(np.zeros((4,)))
print(np.zeros(4))

print(np.ones((2, 7)))

x = np.array(range(0, 10, 2))
print(x)

print(x[3])
print(x[4])
print(x[-1])

print(len(x))
print(x.shape)

C = np.arange(12)
print(C)
C.shape = (3, 4)
print(C)
print(C[0, 0])
print(C[2, 0])
print(C[2, -1])
print(C[-1, -1])

print("Separator po macierzy C")

y = np.arange(10)
print(y)
print(y[0:5])
print(y[0:5:1])
print(y[:5:2])
print(y[0:5:1])
print(y[0:5:-1])
print(y[5:0:-1])
print(y[5:0:-2])
print(y[::-1])

copy_y = y[:]
print(copy_y)

print(C)
print(C[0, :])
print(C[:, 1])
