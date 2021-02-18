
def f(n):
    return 1/n

def sum(n):
    sum=0
    for i in range(n+1):
        if(i==0 or i==n):
            sum+=f(1+2*i/n)
        else:
            sum+=(2*f(1+2*i/n))
    return sum/n

def show(X):
    print(len(X),end=":::")
    for i in X:
        print(i,end=" ")
    print()

n=1
T=[]
for i in range(10):
    T.append(sum(n))
    n*=2

S=[]
for i in range(1,len(T)):
    S.append(4*T[i]/3-T[i-1]/3)

C=[]
for i in range(1,len(S)):
    C.append(16*S[i]/15-S[i-1]/15)

R=[]
for i in range(1,len(C)):
    R.append(64*C[i]/63-C[i-1]/63)

show(T)
show(S)
show(C)
show(R)