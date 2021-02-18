import numpy as np
from sympy import *
import math
x=symbols("x")
#y=pow(x,3)+2*pow(x,2)+exp(x)
#y=sin(x)
y=exp(3*x)
dify=integrate(y)
print(dify)




'''
x=np.linspace(-50,50,100000)
y=[]
u=0
q=10
for i in x:
    y.append(math.exp(-(i-u)**2/(2*pow(q,2)))/(q*(math.sqrt(2*math.pi))))

plt.plot(x,y)
plt.show()
'''




'''
x=[1,2,3,4,5,6,7,8,9,10]
x1=x
y=[1,1.9,3.2,3.8,5.3,6.0,7.3,8.1,8.7,9.7]
arr_mean=np.mean(y)
arr_var=np.var(y)
arr_std=np.std(y)
print(arr_mean)
print(arr_var)
print(arr_std)
print(np.cov(x1,x))

z=np.random.randint(1,100,(10,10))
print(z)
'''

'''
from sympy import *
import math
x=symbols("x")
#y=pow(x,3)+2*pow(x,2)+exp(x)
y=sin(x)
dify=integrate(y,(x,0,math.pi))
print(dify)
print(float(dify))
'''