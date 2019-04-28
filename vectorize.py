# -*- coding:utf8 -*-
from numba import vectorize, float64
import numpy as np


'''
    使用vectorize()装饰器，Numba可以将纯Python函数编译为ufunc，该函数在NumPy数组上运行，与用C语言编写的传统ufunc一样快。

    使用时vectorize()，您可以将函数编写为通过输入标量而不是数组进行操作。Numba将生成周围的循环（或内核），允许对实际输入进行有效迭代。

    该vectorize()装饰有两种操作模式：

    渴望或装饰时间，编译：如果您将一个或多个类型签名传递给装饰器，您将构建Numpy通用函数（ufunc）。本小节的其余部分描述了使用装饰时编译构建ufunc。
    延迟或调用时编译：当没有给出任何签名时，装饰器将为您提供Numba动态通用函数（DUFunc），该函数在使用以前不支持的输入类型调用时动态编译新内核。
    后面的小节“ 动态通用功能 ”更深入地描述了这种模式。
'''
# @vectorize([float64(float64, float64)])
# def f(x, y):
#     return x + y
#
# print(f(10,1.2))

'''
    如果您传递了多个签名，请注意必须在最不具体的签名之前传递大多数特定签名（例如，在双精度浮点数之前单精度浮点数），
    否则基于类型的分派将无法按预期工作：
'''
@vectorize([
    float64(float64, float64)])
def f(x, y):
    return x + y
a = np.linspace(0, 1, 6)
print(f(a,a))

a = np.arange(12).reshape(3, 4)













