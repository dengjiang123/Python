from math import *
import matplotlib.pyplot as plt
from scipy.special import *

P=[]
a=30
b=70
n=50
N=a+b
start=max(n-b,0)
end=min(n,a)

x=[]
for i in range(start,end+1):
    x.append(i)
    P.append(comb(a,i)*comb(b,n-i)/comb(N,n))

print(P)
print(sum(P))
plt.bar(x,P)
plt.show()
print(x[0],x[len(x)-1])

print(1-1/e)