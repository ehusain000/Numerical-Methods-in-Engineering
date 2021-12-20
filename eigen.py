import numpy as np
from scipy import linalg

A = np.array([[4, 1.01],
              [0.01, 4]])

#jacobi(take diagonal)
D,V = linalg.eig(A)

print(D)