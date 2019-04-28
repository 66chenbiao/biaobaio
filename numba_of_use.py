# -*- coding:utf8 -*-
import numba

'''
    概述:
        numba是一个用于编译Python数组和数值计算函数的编译器，这个编译器能够大幅提高直接使用Python编写的函数的运算速度。

        numba使用LLVM编译器架构将纯Python代码生成优化过的机器码，通过一些添加简单的注解，将面向数组和使用大
        量数学的python代码优化到与c，c++和Fortran类似的性能，而无需改变Python的解释器。
'''
'''
    特性:
        动态代码生成 （在用户偏爱的导入期和运行期）
        为CPU（默认）和GPU硬件生成原生的代码
        集成Python的科学软件栈（Numpy）
'''

@numba.jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result















