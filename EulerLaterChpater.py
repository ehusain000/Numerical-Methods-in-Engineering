from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show
def f(x,t):
    return -x**3 + sin(t)


a = 0.0
b = 10.0 # End of the interval
N = 1000 # Number of steps
h = (b-a)/N # Size of a single step
x = 0.0 # Initial condition
tpoints = arange(a,b,h) # t-values of approx. soln x(t)
xpoints = [] # x-values of approx. soln x(t)
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)


plot(tpoints,xpoints)
xlabel("t")
ylabel("x(t)")
show()
