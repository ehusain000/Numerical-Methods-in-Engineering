import numpy as np

A = np.array([[1, 2, 1],
              [3, 8 , 1],
              [0, 4, 1]])

n = 3 # size of A is 3x3

# loop each column j from 0 to (n-2)
for j in range(n-1):
    # loop through each row starting from the second
    for i in range(j+1,n):
        l = (A[j+1,j]/A[j,j]) # first compute multiplier
        A[i,:] = A[i,:] -l*A[j,:] # subtract multiplier*row to eliminate
        
print(A)


        
