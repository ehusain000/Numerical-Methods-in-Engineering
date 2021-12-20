import numpy as np


A = np.array([[7,4],
              [3,6]])


v = np.array([1, 1])


for k in range(16):
    v = A @ v
    
    v = v / np.linalg.norm(v)
    
    lam = np.dot(v, A @ v)
    
    print(k + 1, v, lam)
    
    
    