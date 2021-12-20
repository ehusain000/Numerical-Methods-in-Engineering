def f(x): 
    return x**2 -2

def fPrime(x): 
    return 2*x

x = 1 # initial guess 
print(str(round(0)),str(round(x,14)))

for k in range(7): 
    # 7 iterations
    x = x - f(x)/fPrime(x)
    print(str(round(k)),str(round(x,14)))
    
    
    