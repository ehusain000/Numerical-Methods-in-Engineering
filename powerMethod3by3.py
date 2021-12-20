import numpy as np


A = np.array([[-1, 2, 2],
              [-1, -4, -2],
              [-3, 9, 7]])


v = np.array([1, 0, 0])


for k in range(16):
    v = A @ v
    
    v = v / np.linalg.norm(v)
    
    lam = np.dot(v, A @ v)
    
    print(k + 1, v, lam)
    
    
    