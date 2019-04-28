# -*- coding:utf8 -*-
'''
    基本类型：
        最基本的类型可以通过简单的表达式表达。下面的符号表示主numba模块的属性（因此，如果您读取“boolean”，
        则表示可以访问符号numba.boolean）。根据Numpy的惯例，许多类型都可以作为规范名称和速记别名。
'''
import numba
import numpy as np

'''
    输入名称	速记	评论
    布尔	      B1	表示为一个字节
    uint8，      字节	U1	8位无符号字节
    UINT16	      U2	16位无符号整数
    UINT32	      U4	32位无符号整数
    UINT64	      U8	64位无符号整数
    int8,char	  I1	8位有符号字节
    INT16	      I2	16位有符号整数
    INT32	      I4	32位有符号整数
    Int64的	      I8	64位有符号整数
    INTC	       -	C int大小的整数
    uintc	       -	C int大小的无符号整数
    INTP	       -	指针大小的整数
    uintp	       -	指针大小的无符号整数
    FLOAT32	       F4	单精度浮点数
    float64,double	F8	双精度浮点数
    complex64	    C8	单精度复数
    complex128	   C16	双精度复数
'''
# 一维单精度数组
print(numba.float32[:])

# 相同底层类型的三维数组
print(numba.float32[:, :, :])

# 此语法定义没有特定布局的数组类型（生成接受非连续和连续数组的代码），
# 可以通过：：1在索引规范的开头或结尾使用索引来指定特定的连续性
print(numba.float32[::1])
print(numba.float32[:, :, ::1])
print(numba.float32[::1, :, :])

# 高级类型
'''
    numba.typeof(值)
    创建一个准确描述给定Python值的Numba类型。
    ValueError如果在nopython模式下不支持该值，则引发此 异常。
'''
print(numba.typeof(np.empty(3)))
print(numba.typeof((1, 2.0)))
print(numba.typeof([0]))

#











