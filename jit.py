# -*- coding:utf8 -*-
from numba import jit
import math

@jit
def f(x,y):
    # A somewhat trivial example
    return x + y

'''
    在此模式下，编译将推迟到第一个函数执行。Numba将在调用时推断参数类型，并根据
    此信息生成优化代码。Numba还可以根据输入类型编译单独的特化。例如，f()使用整数或复数调用上面的函数将生成不同的代码路径：
'''
print(f(1, 2))
print(f(1j, 2))

from numba import jit, int32
@jit(int32(int32,int32))
def f(x, y):
    return x + y

'''
    int32(int32, int32)是函数的签名。在这种情况下，相应的特化将由@jit装饰器编译，并且不允许其他专门化。如果您希望对编译器
    选择的类型进行细粒度控制（例如，使用单精度浮点数），这将非常有用。

    如果省略返回类型，例如通过写而不是 ，Numba将尝试为您推断它。函数签名也可以是字符串，您可以将
    其中的几个作为列表传递;
'''
print(f(1, 2))
print(f(2**31, 2**31 + 1))

# 调用和内联其他函数
@jit
def square(x):
    return x ** 2

@jit
def hypot(x, y):
    return math.sqrt(square(x) + square(x))

# 签名规格
'''
    显式@jit签名可以使用多种类型。以下是一些常见的：

    void是什么都不返回的函数的返回类型（None从Python调用时实际返回）
    intp并且uintp是指针大小的整数（分别是有符号和无符号）
    intc并且uintc相当于C int和 整数类型unsigned int
    int8，uint8，int16，uint16，int32，uint32， int64，uint64被（符号和无符号）对应的比特宽度的固定宽度的整数
    float32并且float64分别是单精度和双精度浮点数
    complex64并且complex128分别是单精度和双精度复数
    可以通过索引任何数字类型来指定数组类型，例如，float32[:] 对于一维单精度数组或int8[:,:]对于8位整数的二维数组。
'''

# 编译选项
# 可以将许多关键字传递给@jit装饰器

# nopython
'''
    Numba有两种编译模式：nopython模式和 对象模式。前者产生更快的代码，但有一些限制可以迫使Numba回到后者。为了防止Numba退回，而是提出错误，通过nopython=True。
'''
@jit(nopython=True)
def f(x, y):
    return x + y

from numba import njit, gdb_init
import numpy as np

@njit(debug=True)
def foo(a, index):
  gdb_init() # instruct Numba to attach gdb at this location, but not to pause execution
  b = a + 1
  c = a * 2.34
  d = c[index] # access an address that is a) invalid b) out of the page
  print(a, b, c, d)

bad_index = int(1e9) # this index is invalid
z = np.arange(10)
r = foo(z, bad_index)
print(r)











