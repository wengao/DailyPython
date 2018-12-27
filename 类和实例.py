# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:42:30 2018

@author: Lucy
"""

#面向对象编程
    #类和实例
class student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

A=student('Mike',90)
B=student('Bob',98)

A.print_score()
B.print_score()


#属性私有化，前面加2个下划线 
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_name(self,name):
        self.__name=name
        
    def set_score(self,score):
        self.__score=score
        
A=Student('Mike',90)

  #错误，因为此时只有Student类内部才可以访问属性_name和_score
B=Student('Bob',98)
