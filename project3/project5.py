from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/(1+25*x**2)

x=np.linspace(-1,1,100)
x1=np.linspace(-1,1,5)
x2=np.linspace(-1,1,11)

y=[]
t1=[]
t2=[]

for i in x:
    y.append(f(i))

for i in x1:
    t1.append(f(i))

for i in x2:
    t2.append(f(i))

f1=lagrange(x1,t1)
f2=lagrange(x2,t2)

print(f1)
print(f2)

y1=[]
y2=[]
for i in x:
    y1.append(f1(i))

for i in x:
    y2.append(f2(i))

plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()




'''
from scipy.interpolate import *
from math import *

x=[0.1,0.2,0.3,0.4,0.5]
y=[1.1052,1.2214,1.3499,1.4918,1.6487]
f=lagrange(x,y)
print(f)
print(f(0.285))
print(e**(0.285))
'''

'''def fac(x):
    return np.e**(-0.1*x)*(np.cos(3*x)+np.sin(3*x))

x=np.linspace(0,20,1000)
y=[]
for i in x:
    y.append(fac(i))

plt.plot(x,y)
plt.show()
'''



'''
def fac(x,f):
    return diff(f(x),x,2)+4*diff(f(x),x,1)+13*f(x)

x=symbols('x')
f=Function('f')
pprint(dsolve(fac(x,f),f(x)))



import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,20,1000)
y=[]
for i in x:
    y.append(np.cos(i)+np.sin(i))

plt.plot(x,y)
plt.show()
'''