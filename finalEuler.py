t = 0

y = 0

h = 0.4

print(t, y)

for k in range(3):
    yPrime = t-10*y
    
    deltay = yPrime * h
    
    y = deltay + y
    
    t = t + h
    
    print(round(t, 1), round(y, 4))
    
    