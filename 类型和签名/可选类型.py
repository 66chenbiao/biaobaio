# -*- coding:utf8 -*-
from numba import jit, optional, intp

'''
    class numba.optional（typ ）
    根据底层Numba类型typ创建一个可选类型。可选类型将允许typ或的任何值None
'''
@jit((optional(intp),))
def f(x):
    return x is not None

print(f(0))

