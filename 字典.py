# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:33:33 2018

@author: Lucy
"""

#dict 具有键-值 对
#使用大括号表示
#key是不可变对象
#python中，字符串，整数都是不可变的对象，所以作为key
d={'Michael':95,'Bob':89,'Tracy':87}
d['Michael']
d.get('Michael')

#删除key,value也会删除，因为value是通过key找到的
d.pop('Michael') 

#set 是key的集合，是不可重复的，不可变的

#创建,需要提供一个list或者tuple
s=set([1,2,3]) #list [1,2,3]整体作为一个参数,只需要一个参数就可以了

s=set(1,2,3) #set expected at most 1 arguments, got 3,ERROR
s=set(1,(2,3)) #set expected at most 1 arguments, got 2 ERROR


#添加元素
s.add(4)
#删除key
s.remove(4)



#不可变对象的理解（参考教程）





