from math import  sin
from numpy import arange

def f(x,t): 
    return sin(t) / (1 + x**2)

a = 2
b = 3


N = 9


h = (b-a)/N


tpoints = arange(a,b,h)
xpoints = []
x = 0.0
for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2
    

print(x)



