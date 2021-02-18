import numpy as np

def f(x):
    sum=x/(4+x**2)
    return sum

n=9
start=3
end=6
line=(end-start)/(n-1)
x=np.arange(start,end+line,line)
x=x.tolist()
y=[]
sum=f(x[0])+f(x[-1])
for i in range(2,len(x)-1,2):
    sum+=(2*f(x[i]))

for i in range(1,len(x)-1,2):
    sum+=(4*f(x[i]))
print(sum*line/3)