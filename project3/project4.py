import numpy as np
from math import *
from scipy.stats import *
from sympy import *

A=np.mat([
    [4,-5,2],
    [5,-7,3],
    [6,-9,4]
])

a,b=np.linalg.eig(A)
print(np.around(a))
print(np.around(b))





'''
x=norm.ppf(0.3)
y=norm.ppf(0.05)

print(x)
print(y)

A=np.mat([
    [1,x],
    [1,y]
])
b=np.transpose(np.mat([12800,10000]))
print(np.linalg.solve(A,b))
print(norm.ppf(0.84)*2+15)
print(e**(-1/4)/2)
print((1-norm.cdf(float(sqrt(2)/2))))
print(3*e**(-3)*(1-e**(-1.5))+e**(-4.5))
print(0.7**2)
print(2*0.7**2*0.3)
print(1-0.7**2-2*0.7**2*0.3)

'''



'''alpha=(0.1*norm.cdf((200-220)/25)+(norm.cdf((240-220)/25)-norm.cdf((200-220)/25))*0.001+
      (1-norm.cdf((240-220)/25))*0.2)

y=(1-norm.cdf((240-220)/25))*0.2
print(alpha)
print(y/alpha)
print((1-alpha)**3+3*(1-alpha)**2*alpha)
print((1-0.064)**3+3*0.064*(1-0.064)**2)
'''

'''n=3.52
x=(norm.cdf((25-22.5)/2.5)*0.1+
      (norm.cdf((27.5-22.5)/2.5)-norm.cdf((25-22.5)/2.5))*0.15+(1-norm.cdf((27.5-22.5)/2.5))*0.3)

y=(norm.cdf((25-22.5)/2.5)*0.1)
print(x)
print(1-y/x)
print(1-(1-x)**3)
'''


'''print(sum(map(lambda i,j:i*j,a,b)))
print(np.sum(np.multiply(np.mat(a),np.mat(b))))
print(np.dot(np.array(a),np.array(b)))
print(np.cross(np.array(a),np.array(b)))
'''

'''x=[2880,2440,2700,3500,3500,3600,3080,3860,3200,3100,3180,3200,3300,
   3020,3040,3420,2900,3440,3000,2620,2720,3480,3320,3000,3120,3180,
   3220,3160,3940,2620,3120,2520,3060,2620,3400,2160,2960,2980,3000,
   3020,3760,3500,3060,3160,2700,3500,3080,3100,2860,3500,3000,2520,
   3660,3200,3140,3100,3520,3640,3500,2940,3620,2860,3300,3800,2140,
   3080,3420,2900,3650,3400,2900,2980,3000,2880,3400,3400,3380,3820,
   3240,2640,3020,2520,2400,3420,3640,2700,2700,3500,3440,3240,3120,
   2800,3300,2920,2900,3400,3300,3260,2540,3200,3200,3300,4000,3400,
   3400,2700,2700,2920,3300,3140,2300,2200,3160,2700,2900,3180,3400,
   3160,2440,3640,2620,3100,2980,3200,3100,3260,3100,3160,3540,3100,
   2840,3660,2820,3140,3800,3000,2800,2660,3600,3760,2540,2780,2760,
   2380,3500,3300,3200,3400,3460,3220,3100,3120,3280,2560,2940,2840,
   3400,3420,3400,3500,3740,2820,3100,2820,3880,2500,3400,3540,]

n=len(x)
print(max(x))
print(min(x))

E=np.mean(np.mat(x))
S=sqrt(np.var(np.mat(x)))

print(E)
print(S)
'''


'''
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,16]
y=[3,6,21,46,48,61,52,42,27,11,6,4,1,1,1]

total=sum(y)
E=np.sum(np.multiply(np.mat(x),np.mat(y)))/sum(y)
print(E)

def p(i):
    return e**(-E)*E**i/factorial(i)


ka=0
for i in x:
    #print(i,p(i)*total)
    #print(y[x.index(i)]-p(i)*total)
    ka+=((y[x.index(i)]-p(i)*total)**2/(p(i)*total))

print(ka)
print(chi2.ppf(1-0.05,len(x)-1))
'''

'''
p=[9/16,3/16,3/16,1/16]
n=[315,108,101,32]
s=sum(n)

kafang=sum(map(lambda a,b:(a-s*b)**2/(s*b),n,p))
print(kafang)

print(chi2.ppf(1-0.05,3))
'''

'''
x=[280,101,212,224,379,179,264,222,362,168,250,149,260,485,170,159]

n=len(x)
x=np.mat(x)

e=np.mean(x)
s=sqrt(np.cov(x))
print(e)
print(s)
low=e-t.ppf(1-0.025,n-1)*s/sqrt(n)
hig=e+t.ppf(1-0.025,n-1)*s/sqrt(n)
print(low,hig)
print()

'''

'''a=[61,73,58,64,70,64,72,60,65,80,55,72,56,56,74,65]
b=[83,58,70,56,76,64,80,68,78,108,76,70,97]

na=len(a)
nb=len(b)
a=np.mat(a)
b=np.mat(b)

ea=np.mean(a)
eb=np.mean(b)
sa=sqrt(np.cov(a))
sb=sqrt(np.cov(b))

print(ea)
print(eb)
print(sa**2)
print(sb**2)

f0=sa**2/sb**2
print(f.ppf(0.025,na-1,nb-1))
print(f.ppf(1-0.025,na-1,nb-1))
print(2*f.cdf(f0,na-1,nb-1))

print((ea-eb)/sqrt(sa**2/na+sb**2/nb))

print(t.ppf(0.025,12))
'''

'''
a=[7,-2,15,17,0,-3,1,8,9,-2]
b=[-1,12,-1,-3,3,-5,5,2,-11,-1,-3]
na=len(a)
nb=len(b)

a=np.mat(a)
b=np.mat(b)

ea=np.mean(a)
eb=np.mean(b)
va=sqrt(np.cov(a))
vb=sqrt(np.cov(b))

print(na)
print(nb)
print(ea)
print(eb)
print(va)
print(vb)

print(f.ppf(0.025,na-1,nb-1))
print(f.ppf(1-0.025,na-1,nb-1))

sw=sqrt(((na-1)*va**2+(nb-1)*vb**2)/(na+nb-2))
print(sw**2)
sum=1-t.cdf((ea-eb)/(sqrt(1/na+1/nb)*sw),na+nb-2)
print(sum)
'''

'''A=[16.869,25.050,22.429,8.456,20.589,12.207]
B=[11.074,9.686,12.064,9.351,8.182,6.642]
n=len(A)

A=np.mat(A)
B=np.mat(B)

EA=np.mean(A)
EB=np.mean(B)
SA=sqrt(np.cov(A))
SB=sqrt(np.cov(B))
print(EA,EB)
print(SA,SB)
k=(SA**2/n+SB**2/n)**2/((SA**2/n)**2/(n-1)+(SB**2/n)**2/(n-1))
print(k)

print((EA-EB)/(sqrt(SA**2/n+SB**2/n)))
p=t.cdf(((EA-EB)/(sqrt(SA**2/n+SB**2/n))),6)
print(1-p)
'''

'''x0=chi2.ppf(0.05,24)
print(x0)
print(24*4.25/7)
'''

'''A=[23,35,29,42,39,29,37,34,35,28]
B=[26,39,35,40,38,24,36,27,41,27]
n=len(A)
A=np.mat(A)
B=np.mat(B)

EA=np.mean(A)
EB=np.mean(B)
VA=np.cov(A)
VB=np.cov(B)

E=np.mean(A-B)
print(A-B)
V=sqrt(np.cov(A-B))
print(E)
print(V)
p=t.cdf(E/(V/sqrt(n)),n-1)
print(-2*p)
'''


'''n=25
E=965
V=100
t0=(E-1000)/(V/sqrt(n))
temp=t.ppf(0.05,n-1)
print(t0,temp)
p=t.cdf(t0,n-1)
print(p)
'''



'''x=[15,14.8,15.2,15.4,14.9,15.1,15.2,14.8]
y=[15.2,15,14.8,15.1,14.6,14.8,15.1,14.5,15]

nx=len(x)
ny=len(y)

x=np.mat(x)
y=np.mat(y)

Ex=np.mean(x)
Ey=np.mean(y)
Sx=sqrt(np.cov(x))
Sy=sqrt(np.cov(y))
alpha=0.9

v1=0.18
v2=0.24

print(Ex)
print(Ey)
print(Sx**2)
print(Sy**2)
print(nx)
print(ny)

#sw=sqrt((Sx**2*(nx-1)+Sy**2*(ny-1))/(nx+ny-2))*sqrt(1/nx+1/ny)
sw=sqrt(Sx**2/nx+Sy**2/ny)

hig=Sx**2/(Sy**2*f.ppf(0.05,7,8))
low=Sx**2/(Sy**2*f.ppf(0.95,7,8))

print(low,hig)
'''


'''u1=342
u2=397
n1=19
n2=17
x1=342
x2=397
s1=66.5
s2=89
print(x1-x2+t.ppf(0.025,n1+n2-2)*sqrt(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2))*sqrt(1/n1+1/n2))
print(x1-x2-t.ppf(0.025,n1+n2-2)*sqrt(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2))*sqrt(1/n1+1/n2))
print(((n1-1)*s1*s1+(n2-1)*s2*s2)/(n1+n2-2))
'''


'''x=[3200,3050,2600,3530,3840,4450,2900,4180,2150,2650,2750,3450,2830,3730,3620,2270]
n=len(x)
x=np.mat(x)

E=np.mean(x)
V=sqrt(np.cov(x))
print(E)
print(V)

low=(n-1)*V*V/(chi2.ppf(0.025,n-1))
print(sqrt(low))'''

