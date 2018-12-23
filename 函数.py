# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 18:19:34 2018

@author: Lucy
"""

#函数定义

#做类型检查，只允许传入int类型和float类型的数据
def my_abs(x):
    if (x>0):
        return x
    else:
        return -x
    
    
    
print(my_abs(-3))


#空函数

#pass语句表示什么都不做，作为占位符号
def nop():
    age==17
    if age>18:
        pass
    


def my_abs1(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if(x>0):
        return x
    else:
        return -x
print(my_abs1(1212))


#python支持返回多个值
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    
    return nx,ny
#其实python函数就是返回一个tuple,tuple的圆括号可以省略

x,y=move(100,100,60,math.pi/6)
print(x,y)

r=move(100,100,60,math.pi/6)
print(r)




#可变参数
#没有利用可变参数的情况
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#传入一个list或者tuple
sum=calc([1,2,3])
print(sum)

#使用可变参数’
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
sum2=calc(1,2,3)    #这里就是区别
print('sum %d'%     sum2)



#关键字参数
#上面的参数都是基于位置的，但是关键字参数是基于关键字的。


#**kw表示关键字参数，具有位置特性，又具有可选参数特性
def person1(name,age,**kw):
    print('name:',name,' age:',age,' other:',kw)
person('MIchael',18)
person('Michael',18,city='Beijing',hobby='badminton')


#命名关键字参数--限制关键字参数的名字
#只接受city和job作为关键字参数
def person2(name,age,*,city,job):
    print(name,age,city,job)
person2('Michael',18,city='Beijing',job='teacher')


