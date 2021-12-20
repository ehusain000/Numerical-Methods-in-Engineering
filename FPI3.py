def g(x):
    return x**2 / 3

x = 1


for k in range(21):
    print(k, x)
    
    x = g(x)
    
print(k, x)