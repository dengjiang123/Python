from math import *
import matplotlib.pyplot as plt
from scipy.special import *

s=0

lam=10
t=100
n=1000
p=lam/n

x=[]
y=[]
z=[]
for i in range(t+1):
    x.append(i)
    y.append(e**(-lam)*lam**i/factorial(i))
    z.append(comb(n,i)*p**i*(1-p)**(n-i))


plt.bar(x,y)
plt.plot(x,y)
plt.plot(x,z,1,"test","red")
plt.show()

for i in x:
    print(y[i],z[i])
