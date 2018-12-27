# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:08:57 2018

@author: Lucy
"""

'''
使用__slots__
    但是，如果我们想要限制实例的属性怎么办？
    比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''

class Student(object):
    pass

#给实绑定方法
def set_age(self,name,age):
    self.name=name
    self.age=age

from types import MethodType

#python是一门动态语言，实例可以随时绑定属性和方法
s=Student()
s.name='Michael'

s.set_age=MethodType.MethodType(set_age,s)#给实例绑定方法，这个方法是这个实例特有的，其他的实例是不能调用的
s.set_age(25)

print('对象s的姓名是%s' % s.name)
print('对象的年龄是%d' % s.age)

