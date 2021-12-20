import numpy as np
import matplotlib.pyplot as plt
from math import exp


x0 = 0
f0 = exp(x0)


i = np.r_[-8:0.5:0.5]
h = 10**i
err1 = np.abs((np.exp(x0+h) - f0)/h - 1) #order 1 error
err2 = np.abs((np.exp(x0+h) - np.exp(x0-h))/(2*h) - 1) #order 2 error
err4 = np.abs((np.exp(x0-2*h) - 8*np.exp(x0-h) + 8*np.exp(x0+h) - np.exp(x0+2*h))/(12*h) - 1)


plt.loglog(h,err1)
plt.loglog(h,err2)
plt.loglog(h,err4)
plt.show()


