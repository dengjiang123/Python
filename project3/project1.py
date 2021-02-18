import numpy as np

A=np.mat([
    [2,4,-6],
    [4,2,-6],
    [-6,-6,-15]
])

a,c=np.linalg.eig(A)

print(c)

b=np.mat([
    [1,1,-2],
    [-1,1,-2],
    [0,4,1]
])
print(np.around(np.linalg.inv(b)*A*b))
