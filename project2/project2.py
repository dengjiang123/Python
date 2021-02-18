from math import *

def f(x,y,z):
    s=0
    s=e**(2*x)*sin(x)-2*y+2*z
    return s

x=[]
h=0.1
for i in range(11):
    x.append(h*i)

#print(x)
y=[]
z=[]
y.append(-0.4)
z.append(-0.6)

for i in range(1,11):
    l1=f(x[i-1],y[i-1],z[i-1])
    l2=f(x[i-1]+h/2,y[i-1]+h*z[i-1]/2,z[i-1]+h*l1/2)
    l3=f(x[i-1]+h/2,y[i-1]+h*z[i-1]/2+h**2/4*l1,z[i-1]+h*l2/2)
    l4=f(x[i-1]+h,y[i-1]+h*z[i-1]+h**2/2*l2,z[i-1]+h*l3)
    y.append(y[i-1]+h*z[i-1]+h**2/6*(l1+l2+l3))
    z.append(z[i-1]+h/6*(l1+2*l2+2*l3+l4))

print(x)
print(y)
print(z)
