# -*- coding:utf8 -*-
import numpy as np
from numba import generated_jit, types
'''
    虽然jit()装饰器在许多情况下很有用，但有时您希望根据其输入类型编写
    具有不同实现的函数。所述generated_jit()装饰允许用户控制在编译时的特化的选择，而缩绒一个JIT功能的保持运行时执行速度。
'''

@generated_jit(nopython=True)
def is_missing(x):
    '''
        Return True if th value is missing, False otherwise
    '''
    if isinstance(x, types.float):
        return lambda x: np.isnan(x)
    elif isinstance(x, (types.NPDatetime, types.NPTimedelta)):
        # The corresponding Not-a-Time value
        missing = x('NaT')
        return lambda x: x == missing
    else:
        return lambda x: False

'''
    注意:
        ·使用Numba类型的参数调用修饰函数，而不是它们的值
        ·修饰函数实际上并不计算结果，它返回一个callble，实现给定类型的函数
        ·可以在编译时预先计算一些数据（missing 上面的变量），以便在编译的时候重用
        ·函数定义使用与装饰函数相同的参数名称，这是确保按名称传递参数按预期工作所需的
'''










