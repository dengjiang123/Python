import os

'''
a=[2,3,4,2,2]
b=[1,2,3,4,3]
'''
a=[2,3,4,2,2]
b=[1,2,3,4,3]
c=[2,1,2,2,4]
d=[2,3,1,2,4]



def f(x,n):
    s=0
    for i in range(n+1):
        s+=x[i]
    return s

def buju(x,y,t):
    start=x[0]
    for i in range(1,len(x)):
        temp=f(x,i)-f(y,i-1)
        if(temp>start):
            start=temp
    start+=t
    return start

def show(x,start):
    a='_'
    for i in range(start):
        print(end=" ")
    for i in x:
        for j in range(i):
            print(a,end="")
        if(a=='_'):
            a='-'
        else:
            a='_'
    print()

print("a:",end=" ")

start=0
print("a:",end=" ")
show(a,start)

start=buju(a,b,start)
print("b:",end=" ")
show(b,start)

start=buju(b,c,start)
print("c:",end=" ")
show(c,start)

start=buju(c,d,start)
print("d:",end=" ")
show(d,start)


