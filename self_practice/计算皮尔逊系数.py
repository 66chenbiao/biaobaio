# -*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt


def pearson(x,y):
    x = np.array(x) - np.mean(x)
    y = np.array(y) - np.mean(y)
    z = x * y
    xx = x ** 2
    yy = y ** 2
    # return np.sum(z) / (np.sqrt(np.sum(xx)) * np.sqrt(np.sum(yy)))
    result = np.sum(z) / (np.sqrt(np.sum(xx))*np.sqrt(np.sum(yy)))
    return result


## 调用皮尔逊系数函数
x1 = [5,3,4,4] # 用户1 与物品1-5
x2 = [3,1,2,3] # 用户2 与物品1-5
x3 = [4,3,4,3] # 用户3 与物品1-5
x4 = [3,3,3,5] # 用户4 与物品1-5
x5 = [1,5,2,4] # 用户5 与物品1-5
print(pearson([5, 3, 4, 4], [3, 1, 2, 3]))















