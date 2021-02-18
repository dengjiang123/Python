import xlrd
import os
x=xlrd.open_workbook("ceshi.xls")
print(x)



'''
import numpy as np
from fractions import Fraction

x=[1,2,3,4]
y=[14,18,17,19]
x=np.mat(x)
y=np.transpose(np.mat(y))
a=np.mat([[1,1,1,1],
       [2,4,8,16],
       [3,9,27,81],
       [4,16,64,256]
       ])
b=np.linalg.solve(a,y)
print(b)
for i in range(4):
    print(Fraction(b[i,0]))
'''