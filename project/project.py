from scipy.stats import *
from scipy.special import *
from sympy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

print(norm.pdf(0,0,1))
print(2*norm.cdf(90,80,10)-1)

def f(x,alpha):
    return e**(-x)*x**(alpha-1)

x=symbols('x')
print(integrate(f(x,10),(x,0,100)))
print(1-e**(-10/25),e**(-10/25)-e**(-1),e**(-1))



'''
file=pd.read_csv("附件2.csv",encoding='gb18030')
def f(x,lam):
    return lam*e**(-lam*x)

x=np.linspace(0,5,100)
y=[]
z=[]
w=[]
for i in x:
    y.append(f(i,3))
    z.append(f(i,2))
    w.append(f(i,1))

plt.plot(x,y)
plt.plot(x,z,1,"test","red")
plt.plot(x,w,1,"test","yellow")
plt.show()
'''
