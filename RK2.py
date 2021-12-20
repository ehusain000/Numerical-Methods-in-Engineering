from math import exp

def f(t,Q):
    return -.1 * (Q - 20)


t = 0
Q = 90
h = .01

def q(t):
    return 70 * exp(-.1 * t) + 20

for k in range(2000):
    m1 = f(t, Q)
    m2 = f(t+h, Q + m1 * h)
    
    deltaQ = 0.5 * (m1 + m2) * h
    
    t = t + h
    Q = Q + deltaQ
    

exact = Q
approx = q(20)
print(exact, approx)