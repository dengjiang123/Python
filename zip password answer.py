import zipfile
import time
import threading

startTime = time.time()
# 判断线程是否需要终止
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime - startTime))
        global flag
        # 成功解压其余线程终止
        flag = False
    except Exception as e:
        pass


def do_main():
    zfile = zipfile.ZipFile("temp.zip", 'r')
    # 开始尝试
    for number in range(0,400000):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()


if __name__ == '__main__':
    do_main()



'''
import zipfile

zf=zipfile.ZipFile("temp.zip")
answer=0
for i in range(200000):
    try:
        zf.extractall(pwd=bytes(str(i),"utf8"))
        answer=i
        break
    except:
        pass
    
print(answer)
'''

    

'''import zipfile

zf=zipfile.ZipFile("temp.zip")
p="123456"
zf.extractall(pwd=bytes(p,"utf8"))'''



'''
with zipfile.ZipFile("temp.zip","r") as z:
    for i in range(100000,130000):
        try:
            print(i)
            z.extract("temp.txt",pwd=str(i))
            break
        except:
            pass
'''

'''
with zipfile.ZipFile("temp.zip","r") as z:
    z.extract("temp.txt",pwd=b"123456")
'''
