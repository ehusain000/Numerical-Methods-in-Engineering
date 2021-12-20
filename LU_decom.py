import numpy as np

A = np.array([[1, 2, 1], 
              [3, 8 , 1], 
              [0, 4, 1]])

n = 3 # size of A is 3x3

j = 0 # First Eliminate first column


for i in range(j+1,n): # loop through each row starting from the second 
    l = (A[j+1,j]/A[j,j]) # first compute multiplier 
    A[i,:] = A[i,:] -l*A[j,:] # subtract multiplier*row to eliminate


print(A)

