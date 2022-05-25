from pylab import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# This line configures matplotlib to show figures embedded in the notebook,
# instead of opening a new window for each figure. More about that later.
# If you are using an old version of IPython, try using '%pylab inline' instead.
# %matplotlib inline
# 1.2.1) MATLAB-like API, example
x = np.linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

subplot(1, 2, 1)
plot(x, y, 'r--')
subplot(1, 2, 2)
plot(y, x, 'g*-')
show()

# 1.3) The matplotlib object-oriented API

fig = plt.figure()
axes = fig.add_axes([00.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
show()

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes
# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')
show()
