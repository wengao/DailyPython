# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:57:50 2018

@author: Lucy
"""

#python高级特性
    
#切片
L=['A','B','C']
L[0:3]  #从索引0开始，到索引3结束，但是不包括索引3

L[-1:] #从C开始往后
L[-2:] #['B','C']
L[-3:]
L[:-2] #['A']  #从位置为0开始取,不包括-2位置的元素
L[:-1] #['A','B'] #从位置为0开始取，不包括-1位置的元素

L1=list(range(100))  #0-99
L1[10:20]
L1[:10:2]  #[0,2,4,6,8]
L1[::5]



#使用tuple
L2=(0,1,2,3,4,5)


#针对字符串进行切片操作
#把字符串看做一种list
str='ABCDEF'
str[::2]
L2[:3]















#------迭代操作------
#for...in...
d={'a':1,'b':2,'c':3}  #默认输出key,但是有的时候不是按顺序输出
for key in d:
    print(key)
    
for key in d.keys():
    print(key)
    
for value in d.values(): #输出value
    print(value)
    
#判断是否是可迭代对象
from collections import Iterable
isinstance('abc',Iterable)

#enumerate函数的使用，可以把一个list变成索引-元素对
print('\n\n\n\n\n')
for i,value in enumerate(('A','B','C')):
    print(i,value)
    
for k,v in d.items():  #输出每一对key-value
    print(k,v)
    
    
#查找一个list中的最大值和最小值，返回一个tuple
def findMinAndMax(L):
    min=L[0]
    max=L[0]
   
    for value in L:
        if(min>value):
            min=value
            t=min
            value=t
        if(max<value):
            max=value
            k=max
            value=k
            
    return min,max
        
            

r=findMinAndMax([1,2,3,4])
print(r)


#列表生成式
#用来创建list的生成式子
list(range(1,11))

#生成一个x*x
 
 #导入模块
 import os 
 [d in os.listdir('.')]
 
 
 L=['hello','hi']
 [s.upper() for s in L]
 
 
 
 #生成器
 L=(x*x for x in range(10))


#生成器
g=(x*x for x in range(10))
for n in g:
    print(n)
 
#斐波那契额数列 1 1 2 3 5 8
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

fib(6)


#使用genaator(生成器)实现斐波那契数列
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

#函数中有yield，说明这个函数就是一个geneator，不在是一个普通的函数
#调用该函数的时候，就会生成一个genarator对象，然后用next函数不断获得下一个返回值


#使用迭代器进行杨辉三角定义
    #每一行都是一个list
    #使用迭代器，不断输出下一行的list
def triangles(n):
   for i
       
    

        
