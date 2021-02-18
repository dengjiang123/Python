import numpy as np
from sympy import *
from math import *

A=np.mat([
    [1,2,3],
    [2,1,2],
    [1,3,4]
])

B=np.mat([
    [7,9],
    [4,5]
])

C=np.mat([
    [1,2],
    [1,0],
    [2,3]
])

print(np.linalg.inv(A)*C*np.linalg.inv(B))


'''x=np.mat([
    [7,1,1,8,5],
    [2,2,3,7,2,],
    [4,6,1,7,9],
    [3,6,5,2,1],
    [4,2,3,2,5]
])

print(np.linalg.matrix_rank(x))
print(np.linalg.det(x))
y=np.linalg.inv(x)
print(np.around(y,decimals=10))
'''



'''x=np.random.randint(0,10,(5,5))

print('[',end="")
for i in x:
    print('[',end='')
    temp=i.tolist()
    for j in i:
        if(temp.index(j)<len(temp)-1):
            print(j,end=",")
        else:
            print(j,end="")
    print('],')

'''


'''
x=np.mat([
    [3,7],
    [5,11],
    ])


print(np.mean(x))
print(np.mean(x,0))
print(np.mean(x,1))

print("#######################")
print(np.var(x))
print(np.var(x,0))
print(np.var(x,1))

print("#######################")
print(np.cov(x,0))
print(np.cov(x))
'''

'''
x=np.random.randint(0,100,(10,10))

print('[',end="")
for i in x:
    print('[',end='')
    for j in i:
        print(j,end=",")
    print('],')'''



'''
from sympy import *
from math import *

lam=1/4
alpha=1/4

def P(x,lam):
    return lam*e**(-lam*x)

x=symbols('x')
def f(start):
    return integrate(P(x,lam),(x,start,inf))

answer=solve(f(x)-alpha,[x])
print(answer[0])
'''



'''
import numpy as np
from math import *

x=[1,2,3,4,5,6,7]

print(np.mean(x))
print(np.var(x))
print(np.cov(x))
print(np.std(x))

y=[2,4,6,8,10,12,14]
print(np.cov(x,y)/sqrt((np.cov(x)*np.cov(y))))
'''

'''
from math import *
import scipy

x=[1,2,3,4,5]

x.sort()
print(x)

print("算数平均数:",sum(x)/len(x))
s=1
for i in x:
    s*=i

print("几何平均数:",pow(s,1/len(x)))
temp=0
for i in x:
    temp+=(1/i)

print("调和平均数:",len(x)/temp)
n=10000000
print(pow(n,1/n))

x=[2]
temp=0
for i in range(100):
    temp=x[len(x)-1]
    x.append((2*temp**3+1)/(3*temp**2))

for i in x:
    print(round(i,10))
    '''