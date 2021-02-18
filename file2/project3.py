
n=16
h=1/n
def f(x):
    return 4/(1+x**2)

x=[]
for i in range(n+1):
    x.append(i/n)

y=[]
for i in x:
    y.append(f(i))
print(x)
print(y)
print((2*sum(y)-y[0]-y[-1])/32)

t=3.140941612041389-3.138988494491089
print(t/3)