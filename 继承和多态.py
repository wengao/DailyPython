# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:05:34 2018

@author: Lucy
"""

#继承
class Animal(object):
    def run(self):
        print('Animal is running')

#继承,表示Dog继承自Animal
class Dog(Animal):
    def run(self):
        print('Dog is running')
        
    def eat(self):
        print('Eating meat')
    
   
        
class Cat(Animal):
    
    def run(self):
        print('Cat is running')
        
    def eat(self):
        print('Cat like eating meat')
        

dog =Dog()
dog.run()
#判断实例属于什么类
isinstance(dog,Dog)


cat=Cat()
cat.eat()
isinstance(cat,Cat)



'''
    多态
'''

#这里的animal是Animal的一个实例
def run_twice(animal):
    animal.run()
    animal.run() 
    
c1=Cat()
run_twice(c1)

d1=Dog()
run_twice(d1)

