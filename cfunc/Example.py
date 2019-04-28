# -*- coding:utf8 -*-
'''
    使用scipy.integrate.quad函数。该函数接受常规Python回调或ctypes回调对象中包含的C回调。
'''
import numpy as np
from numba import cfunc
def integrand(t):
    return np.exp(-t) / t**2

nb_integrand = cfunc('float64(float64)')(integrand)
'''
    我们可以将nb_integrand对象的ctypes回调传递给 scipy.integrate.quad并检查结果是否与纯Python函数相同：
'''
import scipy.integrate as si
def do_integrate(func):
    '''
        Integrate the given function from 1.0 to +inf.
    '''
    return si.quad(func, 1, np.inf)

print(do_integrate(integrand))
print(do_integrate(nb_integrand.ctypes))
'''
    使用以编译的回调，集成函数在每次评估被积函数时都不会调用Python解释器
'''