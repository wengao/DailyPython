# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 19:21:14 2018

@author: Lucy
"""

#匿名函数

#冒号前面的x是函数参数，后面的x*x是函数内容
f=lambda x:x*x

#把匿名函数作为返回值，就像前面的章节，函数名可以作为返回值
#只是这里的函数名是匿名的
def build(x,y):
    return lambda:x*x

r=build(3,4)


list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
L=list(filter(lambda n:n%2==1,range(1,50)))
print(L)