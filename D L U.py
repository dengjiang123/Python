import numpy as np
A=np.mat([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,-1,0,-1],[-1,0,-1,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
D=np.mat(np.diag(np.diag(A)))
L=np.mat(np.tril(A,-1))
U=np.mat(np.triu(A,1))

b=np.mat([0,5,-2,5,-2,6])
b=np.transpose(b)

B1=np.linalg.inv(D)*(L+U)
B2=np.linalg.inv(D-L)*U
w1=1.334
w2=1.95
w3=0.95
B31=np.linalg.inv(D-w1*L)*((1-w1)*D+w1*U)
B32=np.linalg.inv(D-w2*L)*((1-w2)*D+w2*U)
B33=np.linalg.inv(D-w3*L)*((1-w3)*D+w3*U)

print(max(map(abs,(np.linalg.eig(B1)[0]))))
print(max(map(abs,(np.linalg.eig(B2)[0]))))
print(max(map(abs,(np.linalg.eig(B31)[0]))))
print(max(map(abs,(np.linalg.eig(B32)[0]))))
print(max(map(abs,(np.linalg.eig(B33)[0]))))

'''print(max(map(fabs,list(np.linalg.eig(B1)[0]))))
print(max(map(fabs,list(np.linalg.eig(B2)[0]))))
print(max(map(fabs,list(np.linalg.eig(B31)[0]))))
print(max(map(fabs,list(np.linalg.eig(B32)[0]))))
print(max(map(fabs,list(np.linalg.eig(B33)[0]))))'''






'''
import numpy as np
A=np.mat([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,-1,0,-1],[-1,0,-1,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]])
D=np.mat([[4,0,0,0,0,0],[0,4,0,0,0,0],[0,0,4,0,0,0],[0,0,0,4,0,0],[0,0,0,0,4,0],[0,0,0,0,0,4]])
L=np.mat([[0,0,0,0,0,0],[-1,0,0,0,0,0],[0,-1,0,0,0,0],[-1,0,-1,0,0,0],[0,-1,0,-1,0,0],[0,0,-1,0,-1,0]])
U=np.mat([[0,-1,0,-1,0,0],[0,0,-1,0,-1,0],[0,0,0,-1,0,-1],[0,0,0,0,-1,0],[0,0,0,0,0,-1],[0,0,0,0,0,0]])

b=np.mat([0,5,-2,5,-2,6])
b=np.transpose(b)

B1=np.linalg.inv(D)*(L+U)
B2=np.linalg.inv(D-L)*U
w1=1.334
w2=1.95
w3=0.95
B31=np.linalg.inv(D-w1*L)*((1-w1)*D+w1*U)
B32=np.linalg.inv(D-w2*L)*((1-w2)*D+w2*U)
B33=np.linalg.inv(D-w3*L)*((1-w3)*D+w3*U)

print(np.tril(A,-1))
print(np.triu(A,1))
print(np.mat(np.diag(np.diag(A))))
'''




'''x="AAAAAA"
y=x.center(20,'#')
print(y)
'''
'''
x=[1,2,3,4,5,6]
y=[7,8,9,10,11]
z=list(map(lambda x,y:x**y,[1,2,3,4,5,6],[7,8,9,10,11]))
print(z)
print(sorted([1,2,3,4,5,6,7,8,9,10],key=lambda x:abs(5-x)))
print(list(filter(lambda x:x%3==0,[1,2,3,4,5,6,7,8])))
'''

'''
from sympy import *

#定义变量
x = Symbol('x')
y = Symbol('y')
print(solve([y-x-40+(x+30)*(1-y/(x+45)),y-2*x+(x+30)*(2-y/x)-25],[x,y]))
print(70+(1-70/105)*90)
print(90*(3-7/6-70/105)+140)
'''
