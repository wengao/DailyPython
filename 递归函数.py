# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:14:42 2018

@author: Lucy
"""

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(3))