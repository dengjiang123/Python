'''
import zipfile
import time
f=open("123.txt","r")
start=time.time()
z=zipfile.ZipFile("temp.zip","r")
x=f.readline().strip("\n")
while x:
    try:
        z.extractall(".",pwd=x.encode("utf-8"))
        print(x)
        break
    except:
        pass
    x = f.readline().strip("\n")

end=time.time()
print(end-start,"s")
'''

import zipfile
import time

start=time.time()
z=zipfile.ZipFile("temp.zip","r")
for i in range(0,400000):
    x=str(i)
    try:
        z.extractall(".",pwd=x.encode("utf-8"))
        print(x)
        break
    except:
        pass
end=time.time()
print(end-start,"s")
