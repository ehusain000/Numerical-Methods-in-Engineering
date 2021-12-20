def f(x): 
    return x**2 -2

a, b= 0, 1 # initial guesses 
print(str(round(0)),str(round(b,8)))

for k in range(11): 
    # 11 iterations
    b = b - (f(b)*(b -a)/(f(b) -f(a)))
    print(str(round(k)),str(round(b,8)))