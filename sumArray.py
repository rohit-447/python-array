import numpy as np

#sumArray takes single arrugument and return its sum
def sumArray(A):
    sum=0
    for i in range(0,len(A)):
        sum=A[i]+sum
        i=i+1
    print(sum)

#array   
A=np.array([2,3,4,5,6])
sumArray(A)