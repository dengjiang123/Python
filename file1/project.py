from math import *

x=[0.7,0.9,1.1,1.3,1.5,1.7]
y=[0.6442,0.7833,0.8912,0.9636,0.9975,0.9917]

t1=len(x)-1
f1=[]
for i in range(t1):
    f1.append((y[i+1]-y[i])/(x[i+1]-x[i]))

f2=[]
for i in range(t1-1):
    f2.append((f1[i+1]-f1[i])/(x[i+2]-x[i]))

f3=[]
for i in range(t1-2):
    f3.append((f2[i+1]-f2[i])/(x[i+3]-x[i]))

print(f1)
print(f2)
print(f3)

print(y[1]+f1[1]*(1-0.9))
print(y[1]+f1[1]*(1-0.9)+f2[1]*(1-0.9)*(1-1.1))
print(y[1]+f1[1]*(1-0.9)+f2[1]*(1-0.9)*(1-1.1)+f3[1]*(1-0.9)*(1-1.1)*(1-1.3))
