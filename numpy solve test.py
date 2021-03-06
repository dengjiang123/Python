import numpy as np

x=np.mat([[51,74,50,58,10,80,15,52,70,31],
[58,85,48,37,35,52,26,34,49,96],
[25,74,24,20,54,58,51,77,15,3],
[51,88,69,54,60,7,39,58,5,55],
[92,39,32,53,90,24,43,90,10,14],
[29,83,92,53,10,56,99,22,62,93],
[86,17,61,43,67,67,21,59,80,13],
[40,88,20,47,87,82,57,44,44,30],
[65,34,65,68,10,83,25,65,5,11],
[38,26,62,45,61,30,64,56,31,77]])
y=np.mat([[51],
[5800],
[2534],
[5112],
[9245],
[2912],
[8677],
[4037],
[6579],
[3837]])

z=np.linalg.solve(x,y)
print(z)
for i in range(10):
    for j in range(10):
        print(x[i,j],end=" ")
    print()
for i in range(10):
    print(y[i,0])
'''
x=np.random.randint(1,100,(10,10))
y=np.random.randint(500,10000,(10,1))
print("[",end='')
for i in range(10):
    print('[',end='')
    for j in range(10):
        print(x[i,j],end=',')
    print('],')
print("[",end='')
for i in range(10):
    print('[',end='')
    print(x[i,0],end='')
    print('],')
'''