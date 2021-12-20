t = 1

y = -2

h = 0.1

print(t, y)

for k in range(25):
    yPrime = t - y
    
    deltay = yPrime * h
    
    y = deltay + y
    
    t = t + h
    
    print(round(t, 1), round(y, 4))
    
    