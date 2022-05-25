import numpy as np

a = np.tile(np.arange(0, 40, 10), (3, 1)).T
print(a)

b = np.array([0, 1, 2])
print(b)

print(a + b)
