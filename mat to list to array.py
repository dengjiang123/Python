import numpy as np
import pandas as pd

mylist = [[1, 2, 3], [4, 5, 6]]  # 列表
print(type(mylist))
print(mylist, end='\n\n')

myarray = np.array(mylist)  # 列表转数组
print(type(myarray))
print(myarray, end="\n\n")

mymatrix = np.mat(mylist)  # 列表转矩阵
print(type(mymatrix))
print(mymatrix, end='\n\n')

MatToArray = np.array(mymatrix)  # 矩阵转数组
print(type(MatToArray))
print(MatToArray, end='\n\n')

ArrayToMat = np.mat(myarray)  # 数组转矩阵
print(type(ArrayToMat))
print(ArrayToMat, end='\n\n')

MatToList1 = mymatrix.tolist()  # 矩阵转列表
print(type(MatToList1))
print(MatToList1)
MatToList2 = list(mymatrix)  # 注意点1
print(type(MatToList2))
print(MatToList2, end='\n\n')

ArrayToList1 = myarray.tolist()  # 矩阵转列表
print(type(ArrayToList1))
print(ArrayToList1)
ArrayToList2 = list(myarray)  # 注意点2
print(type(ArrayToList2))
print(ArrayToList2)
'''
x=np.random.randint(1,100,size=(10,10))
print(x)
print(np.linalg.matrix_rank(x))
'''
'''
y=np.mat([[1,2,3],[4,5,6]])
print(y)
print(np.multiply(y,y))
print(y*y)
x=np.transpose(y)
print(x.dot(y))
'''
#x=np.random.randint(1,100,size=(10,10))
#print(x)
#print(np.linalg.matrix_rank(x))