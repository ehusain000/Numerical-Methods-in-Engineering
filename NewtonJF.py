import numpy as np

def Newton_method(F, DF, x, num_steps):
    
    for k in range(num_steps):
        x = x - np.linalg.solve(DF(x),F(x))
        print(k,x)
        
        

def F(x):
    return np.array([x[0]**2 - 2*x[0] - x[1] + 1, x[0]**2 + x[1]**2 - 1])

def J(x):
    return np.array([[2*x[0] - 2, -1],[2*x[0], 2*x[1]]])

x = np.array([1,3])

Newton_method(F,J,x,5)

