t = 0


S = 45400
I=2100
R=2500

a=0.00001
b=1/14


h = .1 #stepsize

for k in range(3):
    Sprime = - a * S * I
    Iprime = a * S * I - b * I
    Rprime = b * I
    
    print(t, str(round(S, 1)), str(round(I, 1)), str(round(R, 1)))
    
    deltaS = Sprime * h
    deltaI = Iprime * h
    deltaR = Rprime * h
    
    t = t + h
    S = S + deltaS
    I = I + deltaI
    R = R + deltaR
    
    
    

