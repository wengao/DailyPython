# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:27:22 2018

@author: Lucy
"""

'''
    给实例绑定属性的方法是通过实例变量，或者通过self变量
'''
class Student(object):
    def __init__(self,name):
        self.name=name

s=Student('Bob')
s.score=90      #给实例绑定了一个属性


'''
    给类绑定属性的方法是通过实例变量，或者通过self变量
'''
class Student(object):
    def __init__(self,name，score):
        self.name=name
        self.score=score
        

'''
为了统计学生人数，
可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''
class Student(object):
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count+=1

print(Student.count)

print('实例化第一个对象')

#实例化一个对象，就调用一次__init__(self,name)方法
s1=Student('Bob')
print('Student中的count的数目是 %d ' % Student.count)



