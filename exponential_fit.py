import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

a = 1.1
b = 0.3
x = np.linspace(0,10,100)
y = np.exp(a-b*x)

def func(x, av, bv):
    return np.exp(av-bv*x)

def two_fits(x,y):
    popt,pcov = scipy.optimize.curve_fit(func, x, y)
    print("non-linear fit: a=",popt[0]," b=",popt[1])
    fitcoef = np.polyfit(x, np.log(y), 1)
    print("linear fit    : a=",fitcoef[1]," b=",-fitcoef[0])

print("unperturbed:")
two_fits(x, y)
print("\nperturbed:")
yp = y+np.random.random(len(y))
two_fits(x, yp)

