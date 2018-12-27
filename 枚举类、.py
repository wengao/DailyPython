# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:58:17 2018

@author: Lucy
"""

'''
这样的枚举类型定义一个class类型
然后，每个常量都是class的一个唯一实例

value属性则是自动赋给成员的int常量，默认从1开始计数。
'''
from enum import Enum
Month=Enum('Months',('Jan','Feb','Mar','Apr','May','Jun','Jul'))

for name ,member in Month.__members__.items():  #注意是Month,不是Months
    print(name,'=>', member,',',member.value)
 


#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
#@unique装饰器可以帮助我们检查保证没有重复值
from enum import Enum, unique
   
@unique
class Weekday(Enum):
    Sun=0       #Sun是name,0是value,Weekey.Sun是member
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
for name,member in Weekday.__members__.items():
    print(name,'=>',member)
    
    