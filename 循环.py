# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:18:38 2018

@author: Lucy
"""

#使用list或者tuple
#使用type(变量) 判断变量属性

names=['A','B','C']  #定义一个列表
for name in names:
    print(name)
    
#range(100)--生成0，1，2，3，4，的整数序列
#使用list()将range()函数的结果转变成list类型
    
#计算0+1+2+...+100的值
sum =0
for x in range(101):
    sum+=x;
    
#break--结束当前循环
#continue--开始下一次循环

n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print('END')


#只打印奇数
n=0
while n<10:
    n=n+1
    if(n%2==0):
        continue
	print('hahahh')
    print(n)

