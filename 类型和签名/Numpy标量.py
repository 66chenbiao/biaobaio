# -*- coding:utf8 -*-
import numpy as np
import numba

'''
    除了使用之外typeof()，还可以以编程方式构造诸如结构化类型之类的非平凡标量。
'''
struct_dtype = np.dtype([('row', np.float), ('col', np.float)])
ty = numba.from_dtype(struct_dtype)
print(ty)
print(ty[:, :])

'''
    class numba.types.NPDatetime（unit ）
    为给定单位的 Numpy日期时间创建Numba类型。 单元 应该由之中numpy的（例如识别的代码的字符串 Y，M，D等等）。

    class numba.types.NPTimedelta（unit ）
    为给定单位的 Numpy timedeltas创建Numba类型。 单元 应该由之中numpy的（例如识别的代码的字符串 Y，M，D等等）
'''








