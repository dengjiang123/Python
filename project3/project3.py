from scipy.stats import norm
from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

x=[46.2,50.3,48.8,47.7,49.8,46.5,48.3,49.7,48.4,47.2]
x=np.mat(x)
E=np.mean(x)
V=sqrt(np.var(x))
print(E)
print(V)
print(norm.cdf((50-E)/V)-norm.cdf((46-E)/V))



'''x=[1.8,0.5,1.6,0.9,2.0,1.2,1.3,2.5,2.4,0.6]

x=np.mat(x)
E=np.mean(x)
V=sqrt(np.var(x))
print(E)
print(V)
t=1/sqrt(12)
A=np.mat([
    [0.5,0.5],
    [-t,t]
])

b=np.transpose(np.mat([E,V]))

print(np.linalg.solve(A,b))

'''

'''print(gamma(0.5))
print(gamma(1))
x=np.linspace(0,7,1000)
y=[]
for i in x:
    y.append(gamma(i))

plt.plot(x,y)
plt.show()
'''

'''x=[5,10,20,50,100]
p=[0.35,0.3,0.2,0.1,0.05]
x=np.array(x)
p=np.array(p)
E=np.sum(x*p)
E2=np.sum(x*x*p)
var=E2-E**2

print(E)
print(var)

n=156

print(norm.ppf(0.95)*sqrt(n*var)+E*n)
print(norm.cdf((2160-11520/6)/sqrt(11520*5/36)))
print((2160-11520/6)/sqrt(11520*5/36))
print(norm.ppf(0.95)*sqrt(9*15)+150)
'''