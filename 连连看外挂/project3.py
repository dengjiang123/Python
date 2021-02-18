import numpy as np
import cv2
import os
from PIL import Image
import math
import operator
from functools import reduce


name="D:/test/two"
f=open(name+"/temp.txt","r")

file_list=[]
file=f.readline().strip("\n")
while file:
    if file.endswith(".jpg"):
        file_list.append(name+"/"+file)
    file=f.readline().strip("\n")

for i in file_list:
    for j in file_list[file_list.index(i):]:
        img1=cv2.imread(i)
        img2=cv2.imread(j)
        img1=np.float32(img1)
        img2=np.float32(img2)
        first=np.ndarray.flatten(img1)
        second=np.ndarray.flatten(img2)
        differ=np.corrcoef(first,second)
        if differ[0,1]<0:
            differ[0,1]=-differ[0,1]
        if differ[0,1]>0.9:
            print((i[12:-1],j[12:-1],differ[0,1]))
    print()


"""
image1=Image.open(i)
image2=Image.open(j)
img1=image1.histogram()
img2=image2.histogram()
res = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,img1, img2)))/len(img1))
if res<5 and i!=j:
    print((i[12:-1],j[12:-1],res))
"""

