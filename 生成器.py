# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:17:22 2018

@author: Lucy
"""


#不怎么懂生成器
#使用迭代器进行杨辉三角定义
    #每一行都是一个list
    #使用迭代器，不断输出下一行的list
def triangles():
    a=[1]  #a is a list
    x=1
    while (x<3):
        #yield a
        a=a+[0]
        print(a[0]+a[1])
        x=x+1
        a=[a[i-1]+a[i] for i in range(len(a))]
        
        print(a)
        
        
        
    print(type(a))
    
    for i in range(5):
        print(i)


triangles()