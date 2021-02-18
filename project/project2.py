import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from math import *

fig=plt.figure()
ax=Axes3D(fig)

x=np.arange(-4,4,0.01)
y=np.arange(-4,4,0.01)
x,y=np.meshgrid(x,y)

segma1=1
segma2=1
rou=0
def f(x,y,mean,standard_deviation):
    z = np.exp(-((y - mean) ** 2 + (x - mean) ** 2) / (2 * (standard_deviation ** 2)))
    z = z / (np.sqrt(2 * np.pi) * standard_deviation)
    return z

z=f(x,y,0,1)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap="rainbow")
plt.show()
