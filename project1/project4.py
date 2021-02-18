import numpy as np
from math import *
from sympy import *

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

Mc=q1*l**2/2
print("Mc:",Mc)

def f1(x):
    sum=qc+(qd-qc)/h*x
    return sum

def fN(x):
    sum=integrate(f1(a)*(x-a),(a,0,x))
    return sum

x=symbols('x')
a=symbols('a')
Md=Mc+fN(h)
print("Md:",Md)

sigma11a=2*(h**2/2*h*2/3)/Eh
print("sigma11a:",sigma11a)
sigma12a=-2*(h**2/2*l)/Eh
print("sigma12a:",sigma12a)
sigma13a=2*(h**2/2*1)/Eh
print("sigma13a:",sigma13a)

sigma22a=2*(l**2/2*l*2/3)/El+2*(l*h*l)/Eh
print("sigma22a:",sigma22a)
sigma23a=-2*(l**2/2*1)/El-2*(l*h)/Eh
print("sigma23a:",sigma23a)

sigma33a=2*l/El+2*h/Eh
print("sigma33a:",sigma33a)

lt=integrate(fN(x)*x,(x,0,h))/integrate(fN(x),(x,0,h))

delta1a=-2*(Mc*h**2/2+lt*integrate(fN(x),(x,0,h)))
print("delta1a:",delta1a)

delta2a=2*(Mc*l/3*l*3/4)/El+2*(Mc*h*l+integrate(fN(x),(x,0,h))*l)/Eh
print("delta2a:",delta2a)

delta3a=-2*(Mc/3*l*1)/El-2*(Mc*h*1+integrate(fN(x),(x,0,h))*1)/Eh
print("delta3a:",delta3a)

##################

I=b*z**3/12
print("I:",I)
alpha=pow(K*b/(4*E*I*Ell),1/4)
print("alpha:",alpha)

xt=2*l
fai1=cosh(alpha*xt)*cos(alpha*xt)
fai2=cosh(alpha*xt)*sin(alpha*xt)+sinh(alpha*xt)*cos(alpha*xt)
fai3=sinh(alpha*xt)*sin(alpha*xt)
fai4=cosh(alpha*xt)*sin(alpha*xt)-sinh(alpha*xt)*cos(alpha*xt)
print("fai:",fai1,fai2,fai3,fai4)

Md1=-h          ##############################
Ma1=-h          ###################3######################################3
Qd1=Qa1=0
deltaMm1=h
deltaQm1=0
data1=np.mat([
    [b*K/(2*alpha**2)*fai3,b*K/(4*alpha**3)*fai4],
    [b*K/(2*alpha)*fai2,b*K/(2*alpha**2)*fai3]
])
data1=np.mat(data1,dtype='float')

data2=np.transpose(np.mat([-Md1*fai1+Ma1-deltaMm1,Md1*alpha*fai4]))
data2=np.mat(data2,dtype='float')

yd1=np.linalg.solve(data1,data2)[0,0]
setad1=np.linalg.solve(data1,data2)[1,0]
print("yd1:",yd1)
print("setad1:",setad1)

yd1=yd1*(Ell*E*I)
print("yd1:",yd1)

setad1=setad1*(Ell*E*I)
print("setad1:",setad1)

b11=(-h)*setad1
b21=l*setad1+yd1
b31=-setad1
print("b11:",b11)
print("b21:",b21)
print("b31:",b31)

#####################################
Md3=-1
Ma3=-1
Qd3=0
Qa3=0
deltaMm3=1
deltaQm3=0

data31=np.mat([
    [b*K/(2*alpha**2)*fai3,b*K/(4*alpha**3)*fai4],
    [b*K/(2*alpha)*fai2,b*K/(2*alpha**2)*fai3]
])
data31=np.mat(data31,dtype='float')

data32=np.transpose(np.mat([-Md3*fai1-Qd3/(2*alpha)*fai2-deltaMm3+Ma3,
                            Md3*alpha*fai4-Qd3*fai1-deltaQm3+Qa3]))
data32=np.mat(data32,dtype='float')

yd3=np.linalg.solve(data31,data32)[0,0]
setad3=np.linalg.solve(data31,data32)[1,0]
print("yd3:",yd3)
print("setad3:",setad3)
yd3=yd3*(Ell*E*I)
print("yd3:",yd3)

setad3=setad3*(Ell*E*I)
print("setad3:",setad3)
b33=-setad3
print("b33:",b33)
#print(setad1/setad3)
'''
yd3=3.4
setad3=-3.1
b33=3.1
'''
#####################################
print()
print()
Md2=l
Qd2=-1
Ma2=l
Qa2=1
Qf2=-2
fai2alpha=cosh(alpha*xt/2)*sin(alpha*xt/2)+sinh(alpha*xt/2)*cos(alpha*xt/2)
fai1alpha=cosh(alpha*xt/2)*cos(alpha*xt/2)
fai4alpha=cosh(alpha*xt/2)*sin(alpha*xt/2)-sinh(alpha*xt/2)*cos(alpha*xt/2)
print("fai2alpha:",fai2alpha)
print("fai1alpha:",fai1alpha)
print("fai4alpha",fai4alpha)
print()

deltaMm2=-l+2/(2*alpha)*fai2alpha
deltaQm2=-1+2*fai1alpha
print("deltaMm2:",deltaMm2)
print("deltaQm2:",deltaQm2)
'''
deltaMm2=2.142            #######################3
deltaQm2=-1.3696          #########################
'''
data21=np.mat([
    [b*K/(2*alpha**2)*fai3,b*K/(4*alpha**3)*fai4],
    [b*K/(2*alpha)*fai2,b*K/(2*alpha**2)*fai3]
])
data21=np.mat(data21,dtype='float')

data22=np.transpose(np.mat([-Md2*fai1-Qd2/(2*alpha)*fai2-deltaMm2+Ma2,
                            Md2*alpha*fai4-Qd2*fai1-deltaQm2+Qa2]))
data22=np.mat(data22,dtype='float')

yd2=np.linalg.solve(data21,data22)[0,0]
setad2=np.linalg.solve(data21,data22)[1,0]
print("yd2:",yd2)
print("setad2:",setad2)

yd2=yd2*(Ell*E*I)
print("yd2:",yd2)

setad2=setad2*(Ell*E*I)
print("setad2:",setad2)

b22=l*setad2+yd2
b23=-setad2
print("b22:",b22)
print("b23:",b23)
'''
print(-Md2*fai1-Qd2/(2*alpha)*fai2-deltaMm2+Ma2)
print(4.1+4.1*13.2+1/(2*0.4)*(-15)-2.142)
print(Md2*alpha*fai4-Qd2*fai1-deltaQm2+Qa2)
print(1+4.1*0.4*11.3-13.2+1.3696)
'''
print()
###################
Mdp=Md
Qdp=-l*q1
Map=Md
Qap=l*q1
print("Mdp:",Mdp)
print("Qdp:",Qdp)
print("Map:",Map)
print("Qap:",Qap)

deltaMp=-Md
deltaQp=-l*q1

data51=np.mat([
    [b*K/(2*alpha**2)*fai3,b*K/(4*alpha**3)*fai4],
    [b*K/(2*alpha)*fai2,b*K/(2*alpha**2)*fai3]
])
data51=np.mat(data51,dtype='float')

data52=np.transpose(np.mat([-Mdp*fai1-Qdp/(2*alpha)*fai2-deltaMp+Map,
                            Mdp*alpha*fai4-Qdp*fai1-deltaQp+Qap]))
data52=np.mat(data52,dtype='float')
'''
print(-Mdp*fai1-Qdp/(2*alpha)*fai2-deltaMp+Map)
#print(836.96*15.2-198.03*15/0.8)
print(Mdp*alpha*fai4-Qdp*fai1-deltaQp+Qap)
#print(-198.03*11.2+836.96*11.3*0.4)
'''
ydp=np.linalg.solve(data51,data52)[0,0]
setadp=np.linalg.solve(data51,data52)[1,0]
print("ydp:",ydp)
print("setadp:",setadp)

ydp=ydp*(Ell*E*I)
print("ydp:",ydp)

setadp=setadp*(Ell*E*I)
print("setadp:",setadp)

b3p=-setadp
b1p=b3p*h
b2p=-b3p*l+ydp
print("b3p:",b3p)
print("b1p:",b1p)
print("b2p:",b2p)
print()
################3
sigma11=sigma11a+b11
sigma12=sigma12a+b21
sigma13=sigma13a+b31
sigma22=sigma22a+b22
sigma23=sigma23a+b23
sigma33=sigma33a+b33

delta1p=delta1a+b1p
delta2p=delta2a+b2p
delta3p=delta3a+b3p

A=np.mat([
    [sigma11,sigma12,sigma13],
    [sigma12,sigma22,sigma23],
    [sigma13,sigma23,sigma33]
])
bb=np.transpose(np.mat([delta1p,delta2p,delta3p]))
A=np.mat(A,dtype='float')
bb=-np.mat(bb,dtype='float')
print(A)
print(bb)
X=np.linalg.solve(A,bb)
print(X)

x1=X[0,0]
x2=X[1,0]
x3=X[2,0]

############################3
setaDa=0
yDa=0
setaAa=0
yAa=0

QDp=-Qdp+x2
MDp=Md-x1*h+x2*l-x3
print("QDp:",QDp)
print("MDp:",MDp)

fai1a=cosh(alpha*xt/2)*cos(alpha*xt/2)
fai2a=cosh(alpha*xt/2)*sin(alpha*xt/2)+sinh(alpha*xt/2)*cos(alpha*xt/2)
fai3a=sinh(alpha*xt/2)*sin(alpha*xt/2)
fai4a=cosh(alpha*xt/2)*sin(alpha*xt/2)-sinh(alpha*xt/2)*cos(alpha*xt/2)
print("fai:",fai1a,fai2a,fai3a,fai4a)
#######################################################################################3



deltasetaAa=-2*alpha**3/K*fai4a*MDp+2*alpha**2/K*fai3a*QDp
#deltasetaAa=-2*0.4**3/(4*10**4)*2.8397*103.96+2*0.4**2/(4*10**4)*2.4747*80.03
deltayAa=2*alpha**2/K*fai3a*MDp-alpha/(4*K)*fai4a*QDp
#deltayAa=-2*0.4**2/(4*10**4)*2.4747*103.96+0.4/(4*10**4)*80.03*2.8397
print("deltasetaAa:",deltasetaAa)
print("deltayAa:",deltayAa)


deltasetaAa*=10
deltayAa*=10
#deltasetaAa=8.4457*10**(-3)
#deltayAa=17.3252*10**(-3)
##################################################################################33###
data41=np.mat([
    [-2*alpha**3/(b*K)*fai2,-2*alpha**2/(b*K)*fai3],
    [-2*alpha**2/(b*K)*fai3,-1*alpha/(b*K)*fai4]
])
print()

data41=np.mat(data41,dtype='float')

data42=np.transpose(np.mat([-deltasetaAa,-deltayAa]))
#data42=np.transpose(np.mat([-8.4457*10**(-3),-17.3253*10**(-3)]))
data42=np.mat(data42,dtype='float')

print(data41)
print(data42)
MDa=np.linalg.solve(data41,data42)[0,0]
QDa=np.linalg.solve(data41,data42)[1,0]
print("MDa:",MDa)
print("QDa:",QDa)


deltaMf=MDp*fai1a-QDp/(2*alpha)*fai2a
Mf=MDa*fai1a+QDa/(2*alpha)*fai2a+deltaMf
print(MDa,fai1a)
print(QDa,(2*alpha),fai2a)
#yDa*b*K/(2*alpha**2)*fai3a+setaDa*b*K/(4*alpha**3)*fai4a+
print("deltaMf:",deltaMf)
print("Mf:",Mf)