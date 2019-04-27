# -*- coding:utf8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] =False

ax = plt.subplot(111, projection='3d')
ax.scatter([3],[-1],[-1],'c',s=100,label='A')
ax.scatter([5],[1],[5],'r',s=100,label='B')
ax.scatter([-5],[3],[3],'g',s=100,label='C')
ax.set_xlabel('告白')
ax.set_ylabel('起风了')
ax.set_zlabel('放大')
plt.legend()
plt.show()




