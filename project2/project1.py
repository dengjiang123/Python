import numpy as np

a=np.mat([
    [-2,1,0,0],
    [1,-2,1,0],
    [0,1,-2,1],
    [0,0,1,-2]
])

b=np.transpose(np.mat([0.04,0.04,0.04,0.04]))



x=np.linalg.solve(a,b)
print(x)
print(a*x)