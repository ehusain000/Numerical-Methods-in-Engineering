x = 1
def g(x):
    return (x+1)**(1/3)

for i in range(20):
    x = g(x)
    print(i, x)
    