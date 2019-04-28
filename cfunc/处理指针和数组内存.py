# -*- coding:utf8 -*-
'''
    C回调的一个不太重要的用例涉及对调用者传递的某些数据数组进行操作。由于C没有类似于Numpy数组的高级抽象，C回调的签名将传递低级指针和大小参数。然而，
    回调的Python代码将期望利用Numpy数组的强大功能和表现力。

    在以下示例中，C回调预计将在具有签名的二维数组上运行。
    你可以这样实现这样的回调：void(double *input, double *output, int m, int n)
'''
from numba import cfunc, types, carray

c_sig = types.void(types.CPointer(types.double),
                   types.CPointer(types.double),
                   types.intc, types.intc)

@cfunc(c_sig)
def my_callback(in_, out, m, n):
    in_array = carray(in_, (m, n))
    out_array = carray(out, (m, n))
    for i in range(m):
        for j in range(n):
            out_array[i, j] = 2 * in_array[i, j]
'''
    该numba.carray()函数将数据指针和形状作为输入，并返回给定形状的数组视图。
    假设数据按C顺序排列。如果数据以Fortran顺序排列，numba.farray()则应使用。
'''














