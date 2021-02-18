import win32gui
import pyautogui
from PIL import ImageGrab
from PIL import Image
import time
from pynput.mouse import Controller,Button
import math
import cv2
import numpy as np

image=Image.open("test11.jpg")
w,h=image.size
print(w,h)
img_all=image.crop((w/20,h/4,19*w/20,h*9/10))
w,h=img_all.size
print(w,h)

Img_y=[]
img_y=20
add_y=int(h/img_y)
for i in range(img_y):
    Img_y.append(img_all.crop((0,i*add_y,w,(i+1)*add_y)))

differ_N=[]
for i in range(img_y-1):
    Img_y[i].save("AAA.jpg")
    Img_y[i+1].save("BBB.jpg")
    yuan=cv2.imread("AAA.jpg")
    bijiao=cv2.imread("BBB.jpg")
    img1 = np.float32(yuan)
    img2 = np.float32(bijiao)
    first = np.ndarray.flatten(img1)
    second = np.ndarray.flatten(img2)
    differ = np.corrcoef(first, second)
    if differ[0, 1] < 0:
        differ[0, 1] = -differ[0, 1]
    differ_N.append(differ[0,1])

b_y=1
p_y=1
for i in differ_N:
    if(i<0.9):
        b_y=differ_N.index(i)+2
        break
for i in range(len(differ_N)-1,0,-1):
    if(differ_N[i]<0.9):
        p_y=i
        break

print(b_y,p_y)








'''
    differ = np.corrcoef(first, second)
    if differ[0, 1] < 0:
        differ[0, 1] = -differ[0, 1]
    print(differ[0,1])
'''


'''
for i in range(img_y):
    Img_y[i].save("D://test//three/{}.jpg".format(i))
'''