import numpy as np

def jacobi(A, b, x, num_steps):
    
    D  = np.diag(np.diag(A), 0)
    
    for k in range(num_steps):
        r = b - A@x
        
        x = x + np.linalg.inv(D) @ r
        
        print(k+1, x)
        
    return x


A = np.array([[3, -1, 1],
              [3, 6, 2],
              [3, 3, 7]])

b = np.array([1, 0, 4])

x = np.array([0, 0 , 0])

jacobi(A, b, x, 7)

