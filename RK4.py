from math import exp

def f(t,Q):
    return -.1 * (Q - 20)


t = 0
Q = 90
h = .1

def q(t):
    return 70 * exp(-.1 * t) + 20

for k in range(200):
    Q1 = Q
    Q2 = Q + 0.5 * h * f(t, Q1)
    Q3 = Q + 0.5 * h * f (t + 0.5*h, Q2)
    Q4 = Q + h * f(t+ 0.5 * h, Q3)
    
    
    ss= 1/6*(f(t,Q1) + 2*f(t + .5*h, Q2) + 2*f(t+ .5*h, Q3) + f(t + h, Q4))
    
    deltaQ = ss * h
    
    t = t + h
    Q = Q + deltaQ
    

exact = Q
approx = q(20)
print(exact, approx)