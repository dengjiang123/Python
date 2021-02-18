import matplotlib.pyplot as plt
from math import *
x=[]

n=200000
for i in range(n+1):
    x.append(-10+(20/n)*i)

z=[]
y=[]
for i in x:
    y.append(sin(i)*sin(i)*sin(i))
    z.append(cos(i)*cos(i)*cos(i))

#plt.plot(x,y)
plt.plot(y,z)
plt.show()
