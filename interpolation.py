import os
#from scipy.interpolate import lagrange
os.system("dir /a /b *.txt > temp.txt")
file=open("temp.txt")
ft=file.readline().strip("\n")
fx=[]
while ft:
    if(ft!="temp.txt" and ft[0]!='#'):
        fx.append(ft)
    ft=file.readline().strip("\n")
file.close()


def judge4(x):
    m=x.split()
    f=0
    if(float(m[-4])==32766 or float(m[-4])==999990):
        f=1
    return f

def judge5(x):
    m=x.split()
    f=0
    if(float(m[-5])==32766 or float(m[-5])==999990):
        f=1
    return f

def judge6(x):
    m=x.split()
    f=0
    if(float(m[-6])==32766 or float(m[-6])==999990):
        f=1
    return f


def gain_y(xt,j,sum,f):
    x=[]
    z=[]
    for c in range(2*sum+1):
        x.append(c)
        z.append(c)
    n=xt.index(j)
    print(n)
    a,b=0,0
    if f==4:
        x[sum]=int(j.split()[-4])
        z[sum]=n
        for i in range(1, sum +1):
            while (judge4(xt[n-a-i])):
                a+=1
            x[sum-i]=float(xt[n-a-i].split()[-4])
            z[sum-i]=xt.index(xt[n-a-i])
            while (judge4(xt[n+b+i])):
                b+=1
            x[sum+i]=float(xt[n+b+i].split()[-4])
            z[sum+i]=xt.index(xt[n+b+i])
    elif f==5:
        x[sum] = int(j.split()[-5])
        z[sum] = n
        for i in range(1, sum +1):
            while (judge5(xt[n-a-i])):
                a+=1
            x[sum-i]=float(xt[n-a-i].split()[-5])
            z[sum - i] = xt.index(xt[n - a - i])
            while (judge5(xt[n+b+i])):
                b+=1
            x[sum+i]=float(xt[n+b+i].split()[-5])
            z[sum + i] = xt.index(xt[n + b + i])
    elif f==6:
        x[sum] = int(j.split()[-6])
        z[sum] = n
        for i in range(1, sum +1):
            while (judge6(xt[n-a-i])):
                a+=1
            x[sum-i]=float(xt[n-a-i].split()[-6])
            z[sum - i] = xt.index(xt[n - a - i])
            while (judge6(xt[n+b+i])):
                b+=1
            x[sum+i]=float(xt[n+b+i].split()[-6])
            z[sum + i] = xt.index(xt[n + b + i])
    #print(x)
    x1=z[0]
    for i in z:
        z[z.index(i)]-=x1
    #print(z)
    #print(type(x[0]))
    x=x+z
    return x


def interplo(xt,j,n):
    sum = 1
    t=gain_y(xt,j,sum,n)
    y=t[:2*sum+1]
    x=t[2*sum+1:]
    #y=gain_x(xt,x,sum)
    x0= x[sum]
    y0= y[sum]
    del x[sum]
    del y[sum]
    for k in y:
        if(str(k)[:2]=='32'):
            y[y.index(k)]=0
    print(x)
    print(y)
    answer=j.split()
    answer[-n]=str(int((y[0]+y[1])/2))
    answer1=j.replace(str(y0),(str(answer[-n])).center(len(str(y0)),' '),1)
    print(answer1)
    return answer1

def write_file(x,i):
    str1='#'+i
    f=open(str1,"w")
    for j in x:
        f.write(j)
        f.write("\n")
    f.close()


def read(i):
    f=open(i,"r")
    xt=[]
    t=f.readline().strip("\n")
    while t:
        xt.append(t)
        t=f.readline().strip("\n")
    f.close()
    yt=xt[:]
    for j in yt:
        temp=j
        if(judge6(j)):
            #print(j)
            j=interplo(yt,j,6)
            yt[yt.index(temp)]=j
            temp=j
        if (judge5(j)):
            #print(j)
            j = interplo(yt, j, 5)
            yt[yt.index(temp)] = j
            temp = j
        if (judge4(j)):
            #print(j)
            j = interplo(yt, j, 4)
            yt[yt.index(temp)] = j
            temp = j
    write_file(yt,i)


for i in fx:
    print(i)
    read(i)
    print("Congratulation!!!")
os.system("pause")
