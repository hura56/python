import numpy as np
import scipy.optimize
import pylab


def create_data(n):
    """Given an integer n, returns n data points
    x and values y as a numpy.array"""
    xmax = 5
    x = np.linspace(0, xmax, n)
    y = -x ** 2
    # make x-data somewhat irregular
    x += 1.5 * np.random.normal(size=len(x))
    return x, y


def model(x, a, b, c):  # Equation for fit
    return a * x ** 2 + b * x + c


# Main program
n = 10
x, y = create_data(n)
# do curve fit
p, pcov = scipy.optimize.curve_fit(model, x, y)
a, b, c = p
# plot fit and data
xfine = np.linspace(0.1, 4.9, n * 5)
pylab.plot(x, y, 'o', label='data point')
pylab.plot(xfine, model(xfine, a, b, c), label='fit')
pylab.title('fit parameters (a,b,c)=%s' % p)
pylab.legend()
pylab.xlabel('x')
pylab.savefig('curvefit2.pdf')
pylab.show()
