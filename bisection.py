def bisection(a, b, n):
    for i in range(n):
        m = (a + b) / 2 
        if f(a)*f(m) < 0:
            b = m 
        elif f(a)*f(m) > 0: 
            a = m 
        else:
            return m 
    return (a + b) / 2

def f(x):
    return x**3 + 4* x**2 -10

(bisection(1, 2, 10)))