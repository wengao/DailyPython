# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:14:35 2018

@author: Lucy
"""

import functools

int2=functools.partial(int,base=2)


'''
    functools.partial就是帮助我们创建一个偏函数的，
    不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：


'''