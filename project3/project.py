import numpy as np

X=np.mat([-1,0,1,2])
Y=np.transpose(np.mat([4,1,-1,-1]))
A=np.mat([
    [1,1,1,1],
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1]
])

A=A/2
beita=np.array([0,0,1,1])

c=np.transpose(np.mat([3,2,4,-5]))
x=(A*c).sum(1)

x=np.array(np.transpose(x))[0]
print(x)

print(np.sqrt(x.dot(x)))
print(x.dot(beita))