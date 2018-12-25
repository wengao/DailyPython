# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:24:50 2018

@author: Lucy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
    
    
#作用域
def _private_1(name):  #private范围，前面用‘_’表示私有
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name #private范围

def greeting(name):        #public范围
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
