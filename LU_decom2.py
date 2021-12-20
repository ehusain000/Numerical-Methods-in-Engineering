import numpy as np

A = np.array([[1, 2, 1],
              [3, 8 , 1],
              [0, 4, 1]])


print("A = ", A)

n = 3 # size of A is 3x3 
L = np.identity(n)


for j in range(n-1): 
    # loop each column j from 0 to (n-2)
    for i in range(j+1,n):
        # loop through each row starting from the second
        L[i,j] = (A[j+1,j]/A[j,j]) # first compute multiplier
        A[i,:] = A[i,:] -L[i,j]*A[j,:] # subtract multiplier*row to eliminate
        
        
U = A

print("L: ", L)
print("U: ", U)