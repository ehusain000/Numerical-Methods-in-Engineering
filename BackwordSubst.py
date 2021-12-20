import numpy as np

U = np.array([[1, 2, 1],
              [0, 2 , -2], 
              [0, 0, 5]])


n = 3 # size of A is 3x3


b = np.array([2,6,-10]) # U and b from classwork

x = np.zeros(n,float) # empty vector x to hold answer

for i in range(n-1,-1,-1):
    # loop backwards, starting at end
    x[i] = b[i]
    for j in range (i+1,n):
        # for each column greater than i
        x[i] -= U[i,j]*x[j]
    x[i] = x[i]/U[i,i]

print("x = " , x)



