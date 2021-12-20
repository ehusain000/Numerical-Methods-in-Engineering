from math import log, exp, sqrt

def g(x):
    return 7 - exp(x)


x = 1

for k in range(8):
    print(k,x)
    
    x = g(x)
    
    
print(k,x)