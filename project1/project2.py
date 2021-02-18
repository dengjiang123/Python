import matplotlib.pyplot as plt
import numpy as np
from math import *

x=np.linspace(1,10000001,10000000)

def f(n):
    sum=1.0
    for i in range(1,n+1,1):
        sum*=(1+1/n)
    return sum

y=[]

print(f(100000000))
print(e)