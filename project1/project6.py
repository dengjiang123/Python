import matplotlib.pyplot as plt
from sympy import *
import numpy as np

l=4.1
h=4.73
q1=48.3
qc=16
qd=83.6
El=2.6
Eh=1
Ell=1.95
z=0.5
K=4*10**4
b=1
E=2*10**7
E0=5000

x1=76.3
x2=-118.0
x3=-111.7
def f1(x):
    sum=qc+(qd-qc)/h*x
    return sum

def fN(x):
    #sum=integrate(f1(a)*(x-a),(a,0,x))
    sum=-4.764*x**3 + x**2*(7.146*x - 8.0) + 16.0*x**2
    return sum

x=symbols('x')
a=symbols('a')
print(fN(x))



xline=np.linspace(0,4.73,1000)
def fy(i):
    sum=-x1*i+4.1*x2-1*x3+fN(i)+405.96
    print(i,sum)
    return sum

yline=[]
for i in xline:
    yline.append(fy(i))

plt.plot(xline,yline)
plt.show()