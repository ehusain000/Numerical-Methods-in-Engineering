def f(x):
    return x**3 + 4* x**2 -10

tol = 1e-7

a = 1
b = 2

n = 0


while (b-a) > tol:
    x = 0.5 * (a+b)
    
    if f(a) * f(x)< 0:
        b = x
    else:
        a = x
        
    n = n + 1
    
    print(n, x)
    

    
    
