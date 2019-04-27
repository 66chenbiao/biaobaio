# -- encoding:utf-8 --
import numpy as np
def pearson(x, y):
    x = np.array(x) - np.mean(x)
    # print(x)
    y = np.array(y) - np.mean(y)
    # print(y)
    z = x * y
    xx = x ** 2
    yy = y ** 2
    return np.sum(z) / (np.sqrt(np.sum(xx)) * np.sqrt(np.sum(yy)))
#print(pearson([5, 4, 4, 5], [3, 2, 2, 3]))
print("_____")
print(pearson([5, 3, 4, 4], [3, 1, 2, 3]))
print(pearson([5, 3, 4, 4], [4, 3, 4, 3]))
print(pearson([5, 3, 4, 4], [3, 3, 3, 5]))
print(pearson([5, 3, 4, 4], [1, 5, 2, 4]))
#print(4 + (0.8528 * (3 - np.mean([3, 1, 2, 3]) + 0.707 * (5 - np.mean([4, 3, 4, 3])))) / (0.8528 + 0.707))
#print((3 - np.mean([3, 1, 2, 3])))

print("+"*10)
def pearson(x, y):
    x = np.array(x)
    y = np.array(y)
    z = x * y
    xx = x ** 2
    yy = y ** 2
    return np.sum(z) / (np.sqrt(np.sum(xx)) * np.sqrt(np.sum(yy)))

print(pearson([1, -1, 0, 0], [0.6, -1.4, -0.4, 0.6]))
print(pearson([1, -1, 0, 0], [0.2, -0.8, 0.2, -0.8]))
print(pearson([1, -1, 0, 0], [-0.6, -0.6, -0.6, 1.4]))
print(pearson([1, -1, 0, 0], [-1.6, 2.4, -0.6, 1.4]))
#
#
print("**"*10)
print(pearson([0.6, 1.2, 0.4, -1.6], [0.6, 0.2, -0.6, -1.6]))
print(pearson([0.6, 1.2, 0.4, -1.6], [-1.4, -0.8, -0.6, 2.4]))
print(pearson([0.6, 1.2, 0.4, -1.6], [-0.4, 0.2, -0.6, -0.6]))
print(pearson([0.6, 1.2, 0.4, -1.6], [0.6, -0.8, 1.4, 1.4]))


