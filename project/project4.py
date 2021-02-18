from scipy import stats
from scipy.special import *
import numpy as np

n=1000
p=0.005
t=2

s=0
for i in range(t+1):
    print(comb(n,i)*p**i*(1-p)**(n-i))
    s+=(comb(n,i)*p**i*(1-p)**(n-i))

print(1-s)