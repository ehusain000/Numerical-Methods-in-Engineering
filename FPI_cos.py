from math import cos

def g(x):
    return cos(x)

x = 1


for k in range(21):
    print(k, x)
    
    x = g(x)
    
print(k, x)