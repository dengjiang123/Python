
f=open("123.txt","w")
import os
import time
def fac(n):
    if(n<=1):
        return n
    elif(n==2):
        return 1
    elif(n==3):
        return 2
    elif(n==4):
        return 3
    else:
        return 3*fac(n-5)+5*fac(n-4)

n=eval(input())
start=time.time()
for i in range(n+1):
    f.write(str(i)+"  "+str(fac(i))+"\n")
    print(i,fac(i))

end=time.time()
print(str(end-start))
f.write(str(end-start))
os.system("pause")