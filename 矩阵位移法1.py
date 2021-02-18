import numpy as np

#b=0.4
#h=0.6
E=2*10**8
A=270*10**(-4)
I=1.71*10**(-3)
A1=5.4*10**(-4)
I1=0

def get_K(E,A,I,l):
    Ke=np.mat([
        [E*A/l,0,0,-E*A/l,0,0],
        [0,12*E*I/l**3,6*E*I/l**2,0,-12*E*I/l**3,6*E*I/l**2],
        [0,6*E*I/l**2,4*E*I/l,0,-6*E*I/l**2,2*E*I/l],
        [-E*A/l,0,0,E*A/l,0,0],
        [0,-12*E*I/l**3,-6*E*I/l**2,0,12*E*I/l**3,-6*E*I/l**2],
        [0,6*E*I/l**2,2*E*I/l,0,-6*E*I/l**2,4*E*I/l],
    ])
    return Ke

def get_T(alpha):
    T=np.mat([
        [np.cos(alpha),np.sin(alpha),0,0,0,0],
        [-np.sin(alpha),np.cos(alpha),0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,np.cos(alpha),np.sin(alpha),0],
        [0,0,0,-np.sin(alpha),np.cos(alpha),0],
        [0,0,0,0,0,1]
    ])
    return T

def get_angle(n):
    return n/180*np.pi

k1=get_K(E,A,I,12)
t1=get_T(get_angle(0))
K1=np.transpose(t1)*k1*t1
lab1=[0,0,0,1,2,3]

k2=get_K(E,A,I,12)
t2=get_T(get_angle(0))
K2=np.transpose(t2)*k2*t2
lab2=[1,2,3,0,0,0]

k3=get_K(E,A1,I1,15)
t3=get_T(get_angle(217))
K3=np.transpose(t3)*k3*t3
lab3=[1,2,3,0,0,0]

print(np.around(K1,5))
print(np.around(K2,5))
print(np.around(K3,5))

n=3
F=np.transpose(np.mat([0,60,120]))
K=np.mat(np.full((n,n),0.0))

K1=np.array(K1)
K2=np.array(K2)
K3=np.array(K3)
K=np.array(K)
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i in lab1) and (j in lab1):
            K[i-1][j-1]+=K1[lab1.index(i)][lab1.index(j)]
        if (i in lab2) and (j in lab2):
            K[i-1][j-1]+=K2[lab2.index(i)][lab2.index(j)]
        if (i in lab3) and (j in lab3):
            K[i-1][j-1]+=K3[lab3.index(i)][lab3.index(j)]

K=np.mat(K)
delt=np.linalg.solve(K,F)

print(delt,end="#####################\n")

def get_delta(lab):
    f=[]
    for i in range(6):
        if lab[i] != 0:
            f.append(float(delt[lab[i]-1][0]))
        else:
            f.append(0)
    return np.transpose(np.mat(f))

delta1=get_delta(lab1)
delta2=get_delta(lab2)
delta3=get_delta(lab3)

print(np.transpose(delta1))
print(np.transpose(delta2))
print(np.transpose(delta3))

F1=k1*t1*delta1
F2=k2*t2*delta2
F3=k3*t3*delta3

print(np.transpose(np.mat(F1)))
print(np.transpose(np.mat(F2)))
print(np.transpose(np.mat(F3)))
