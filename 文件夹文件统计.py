import os
path=os.getcwd()
count=0
for root,dirs,files in os.walk(path):
    for each in files:
        print(each)
        count+=1
print(count)
os.system("pause")
