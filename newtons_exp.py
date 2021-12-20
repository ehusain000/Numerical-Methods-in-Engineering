from math import exp

def f(x):
    return exp(x) + x - 7

def fPrime(x):
    return exp(x) + 1


x = 1

for k in range(8):
    print(k,x)
    
    x = x - f(x)/fPrime(x)
    
print(k+1,x)
