# -*- coding:utf8 -*-
from numba import cfunc

'''
    与某些本机库（例如，用C或C ++编写）连接可能需要编写本机回调以向库提供业务逻辑。该numba.cfunc()装饰创建编译函数从国外的C代码调用，使用您所选择的签名。
'''

@cfunc('float64(float64, float64)')
def add(x, y):
    return x + y

'''
    C函数对象将已编译的C回调的地址公开为address属性，以便您可以将其传递给任何外部C或C ++库。它还公开了一个ctypes指向该回调的回调对象; 
    该对象也可以从Python调用，从而可以轻松检查已编译的代码
'''
print(add.ctypes(4.0, 5.0)) # prints '9.0'













