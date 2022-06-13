import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 50)
y1 = (-x) ** 3 + 3*x - 7
y2 = 4*x + 6
y3 = 4*(x ** 3) + 6

fig, ax = plt.subplots()

ax.plot(x, y1, 'b.-', label='(-x)^3 + 3*x - 7')
ax.plot(x, y2, 'g--', label='4*x + 6')
ax.plot(x, y3, 'y-', label='4*(x ^ 3) + 6')
ax.grid()
ax.legend(loc=2)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title("Wykresy")
plt.savefig("wykresy.pdf")
plt.show()
