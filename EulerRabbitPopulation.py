t = 0
y = 100

h = .001

print (t, y)

for k in range(37000):
    yPrime = .1 * y * (1 - y/1000)
    
    deltay = yPrime * h
    
    t = t + h
    y = y + deltay
    

print (str(round(t,3)), str(round(y, 3)))