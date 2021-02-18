import numpy as np

x=np.mat([
    [-1,1,0],
    [0,3,0],
    [1,0,2]
])

a,b=np.linalg.eig(x)
print(a)
c1=b[:,0]
c2=b[:,1]
c3=b[:,2]
print(c1)
print(c2)
print(c3)

print(x*c3)
print(a[2]*c3)

print("############")

print(np.diagonal(x))


