from math import *

def f(x):
    #return sqrt(1+3*sin(x)**2)
    return 1

def get_x(n,i):
    return ((pi/n)*i)/2

def show(x):
    for i in x:
        print(i,end=" ")
    print(i)

def sum_T(x):
    sum=0.0
    for i in x:
        sum+=(2*i)
    sum-=x[0]
    sum-=x[len(x)-1]
    return sum*(pi/4)/(len(x)-1)

T=[]
n=1
temp_T=0
while True:
    for i in range(n+1):
        if(i<len(T)):
            T[i]=f(get_x(n,i))
        else:
            T.append(f(get_x(n,i)))
    if fabs(sum_T(T)-temp_T)<0.0000000001:
        break
    show(T)
    temp_T=sum_T(T)
    print(temp_T)
    n*=2

print(len(T),sum_T(T))