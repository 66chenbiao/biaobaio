# -*- coding:utf8 -*-
import numpy as np
from numba import jitclass
from numba import int32, float32
'''
    Numba通过numba.jitclass() 装饰器支持类的代码生成。可以使用此装饰器标记类以进行优化，同时指定每个字段的类型。我们将生成的类对象称为jitclass。jitclass的所有方法都被编译成nopython函数。jitclass实例的数据在堆上作为C兼容结构分配，以便任何已编译的函数可以绕过解释器直接访问底层数据。
'''

spec = [
    ('value', int32), # a simple scalar fiele
    ('array', float32[:]), # an array field
]

@jitclass(spec)
class Bag(object):
    def __init__(self,value):
        self.value = value
        self.array = np.zeros(value, dtype=np.float32)

    @property
    def size(self):
        return self.array.size

    def increment(self, val):
        for i in range(self.size):
            self.array[i] = val
        return self.array
'''
    在上面的例子中，a spec被提供为2元组的列表。元组包含字段的名称和字段的numba类型。
    或者，用户可以使用字典（OrderedDict优选用于稳定字段排序），其将字段名称映射到类型。

    该类的定义至少需要__init__一种初始化每个定义字段的方法。未初始化的字段包含垃圾数据。
    可以定义方法和属性（仅限getter和setter）。它们将自动编译。
'''









