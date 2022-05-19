import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

fig, axes = plt.subplots(1, 2, figsize=(10,3))
#domyslna siatka
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)
#customowa siatka
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', lw=0.5)

plt.show()