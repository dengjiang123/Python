import math
import numpy as np

t=[0.4,0.5,0.6,0.7]
I=[1.75,1.34,1.00,0.74]

a11=len(t)
a12=sum(t)
a21=sum(t)
a22=sum(map(lambda x:x*x,t))

A=np.mat([
    [a11,a12],
    [a21,a22]
])

b1=sum(map(lambda x:math.log(x),I))
b2=sum(map(lambda x,y:math.log(x)*y,I,t))
b=np.transpose(np.mat([b1,b2]))

x=np.linalg.solve(A,b)
print(x)
print(math.e**1.71895282)