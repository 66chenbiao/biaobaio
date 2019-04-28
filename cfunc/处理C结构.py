# -*- coding:utf8 -*-
'''
    对于具有大量状态的应用程序，在C结构中传递数据很有用。为了简化与C代码的互操作性，
    numba可以使用以下方法将cffi类型转换为numba Record类型 numba.cffi_support.map_type：
'''
from cffi import FFI
from numba import cffi_support, types

src ="""
/* Define the C struct */
typedef struct my_struct {
   int    i1;
   float  f2;
   double d3;
   float  af4[7]; // arrays are supported
} my_struct;

/* Define a callback function */
typedef double (*my_func)(my_struct*, size_t);
"""

ffi = FFI()
ffi.cdef(src)

# Get the function signature from *my_func*
sig = cffi_support.map_type(ffi.typeof('my_func'), use_record_dtype=True)

# Make the cfunc
from numba import cfunc, carray

@cfunc(sig)
def foo(ptr, n):
    base = carray(ptr, n) # view pointer as an array of my_struct
    tmp = 0
    for i in range(n):
        tmp += base[i].i1 * base[i].f2 / base[i].d3
        tmp += base[i].af4.sum() # nested arrays are like normal numpy array

    return tmp

# 用numba.types.Record.make_c_struct
my_struct = types.Record.make_c_struct([
    # Provides a sequence of 2-tuples i.e.（name:str, type:Type）
    ('i1', types.int32),
    ('f2', types.float32),
    ('d3', types.float64),
    ('af4', types.NestedArray(dtype=types.float32, shape=(7,))),
])
# 由于ABI限制，结构应types.CPointer(my_struct)作为参数传递，作为参数类型。
# 在cfunc 身体内部，my_struct*可以访问carray。






