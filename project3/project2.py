from scipy.stats import *
import numpy as np
import matplotlib.pyplot as plt

print(chi2.ppf(0.9,25))
print(2-2*t.cdf(2,5))
n1=5
n2=20

print(f.ppf(0.1,n1,n2))
print(1/f.ppf(0.9,n2,n1))
print(f.ppf(0.9,9,10))
print(1-f.cdf(3,9,10))



x=np.linspace(0,100,1000)
y=[]
z=[]

k=25
for i in x:
    y.append(chi2.cdf(i,k))
    z.append(chi2.pdf(i,k))

plt.plot(x,y)
plt.plot(x,z)
#plt.show()
