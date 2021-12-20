
a = 8

def f(x):
    return (x-a)** 3
    
def fPrime(x):
    return 3 * (x - a)**2 

x = 1
k = 0

print(k , x)

ftol = 1e-8

while abs(f(x)) > ftol:
    x = x - f(x) / fPrime(x)
    
    k = k + 1
    
    print(k , x)