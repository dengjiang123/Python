import linecache
import os
os.system("dir /a /b *.txt >temp.txt")
n=1   #修改行数
line="#line"+str(n)+".txt"
file=open(line,"w")
f=open("temp.txt","r")
x=f.readline().strip('\n')
while(x):
    print(x)
    if(x=="temp.txt" or x[0:4]=="#line"):
        pass
    else:
        file.write(linecache.getline(x,n))
    x = f.readline().strip('\n')
file.close()