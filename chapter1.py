from math import sin, cos

h = 0.1




for k in range (1, 13):
    exact = cos(1.2)
    approx = (sin(1.2 + h) - sin (1.2))/h
    error = abs(exact - approx)
    
    print("h", k)
    print("exact: ", exact)
    print("approx:", approx)
    print("error", error)
    
    h = h/10
    
    print(' ')


