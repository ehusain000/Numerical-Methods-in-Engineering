t = 0
h = 0.1
R = 0.072

print(t, R)

for k in range(400):
    Rprime = -1/2337 * R
    
    deltaR = Rprime * h
    
    
    t = t + h
    R = R + deltaR
    print(t, R)
    
    
    