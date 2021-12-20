from math import exp
# approximate the derivative to f at x0
def f(x):
    return exp(x)


x0 = 0
for k in range(1,6):
    h = 10**(-k)
    fPrime1 = (f(x0+h) - f(x0-h))/(2*h) # 3pt approximate derivative
    fPrime2 = (f(x0+h/2) - f(x0-h/2))/(2*(h/2)) # 2nd 3pt approximate derivative
    fPrime_better = (4*fPrime2 - fPrime1)/3 # mix of two 3pt approximates
    err = abs(fPrime_better - 1) # absolute error
    print(k,h,err)