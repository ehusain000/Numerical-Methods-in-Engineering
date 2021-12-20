from math import exp

def f(x):
    return exp(x) + x - 7

x0 = 0
x1 = 1

for k in range(8):
    x0, x1= x1, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    print(k, x0)
    
print(k+1,x1)