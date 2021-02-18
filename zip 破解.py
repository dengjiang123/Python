

#多线程zip破解
'''
import zipfile
import time
import threading

flag=True
start=time.time()

def extract1(p,file):
    try:
        file.extractall(pwd=bytes(p,"utf-8"))
        print(p)
        end=time.time()
        print(end-start)
        global flag
        flag=False
    except:
        pass

zf=zipfile.ZipFile("temp.zip")
for i in range(200000):
    print(i)
    if flag is True:
        t=threading.Thread(target=extract1,args=(str(i),zf))
        t.start()
        t.join()

end1=time.time()
print(end1-start)
'''

#最简单zip破解

import zipfile
import time

start=time.time()
zf=zipfile.ZipFile("temp.zip")

answer=0
with open("password.txt") as file:
    for i in file:
        i=i.strip("\n")
        try:
            zf.extractall(pwd=bytes(i,"utf-8"))
            answer=i
        except:
            pass

print(answer)
end=time.time()

print(end-start)
