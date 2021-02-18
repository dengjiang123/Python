import threading
import time

def fac(n):
    if n<=1:
        return n
    else:
        return fac(n-1)+fac(n-2)

class MyThread(threading.Thread):
    def __init__(self,fac,args=()):
        super(MyThread,self).__init__()
        self.fac=fac
        self.args=args

    def run(self):
        self.result=self.fac(*self.args)
        #print(*self.args,end=" ")

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

n=30
start=time.time()
for i in range(n+1):
    t=MyThread(fac,args=(i,))
    t.start()
    t.join()
    print(t.get_result())

end=time.time()
print(end-start)