import os
import time
start=time.time()

x=[]
file=os.listdir(os.getcwd())
for i in file:
    if (i[-1]=='t' or i[-1]=='T') and (i[-2]=='x' or i[-2]=='X') and (i[-3]=='t' or i[-3]=='T') and i[-4]=='.' and i!="12.txt" and i!="123.txt" and i!="##answer##.txt":
        x.append(i)
#print(x)

f1=open("123.txt","r")
y=[]
y1=f1.read().split()
for i in y1:
    y.append(int(i))
print(y)

f=open("##answer##.txt","w")

def judge(n):
    f=0
    for i in y:
        if i==n:
            f=f+1
        #print(i, n)
    #print(f)
    return f

for i in x:
    f2=open(i,"r")
    z=f2.readline()
    while z:
        t=int(z.split()[0])
        #print(t)
        if judge(t):
            f.write(z)
            #print(z)
        z=f2.readline()

end=time.time()
print(int((end-start)*1000))