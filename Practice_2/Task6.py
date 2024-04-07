import numpy as np
def nonzero(A):
 for i in range(len(A)):
    for j in range(len(A[i])):
        if (A[i][j]!=0):
           return i,j

A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))