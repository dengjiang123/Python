import zipfile
import time

zf=zipfile.ZipFile("temp.zip")
answer=0
start=time.time()
n=400000
for i in range(n):
    try:
        zf.extractall(pwd=bytes(str(i),"utf-8"))
        answer=i
        break
    except:
        pass

end=time.time()
print(answer)
print(end-start)
