import numpy as np
import scipy
import scipy.linalg

A = np.array([[7, 4],
              [3, 6]])


P, L, U = scipy.linalg.lu(A)

v = np.array([1, 1])

for k in range(7):
    
    c = np.linalg.solve(L, P@v)
    
    v = np.linalg.solve(U, c)
    
    v = v / np.linalg.norm(v)
    
    lam = np.dot(v, A @ v)
    
    print(k+1, v, lam)
    
    
    