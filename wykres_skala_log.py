import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale('log')
axes[1].set_title('logarithmic scale (y)')


plt.show()