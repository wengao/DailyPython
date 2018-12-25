# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:00:06 2018

@author: Lucy
"""

'''

函数名也是变量
那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，
完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

'''

#高阶函数
#把函数作为函数的参数，此时的函数就是高阶函数
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))


def f(x):
    return x*x
list1=[1,2,3,4,5]
r=map(f,list1)   #此时r是一个迭代器，是惰性序列,针对list中的每一个元素
list(r)

#reduce的用法
from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,3,5,7,9])



#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
#作用：str转换成int类型
from functools import reduce
def fn(x,y):
    return x*10+y



#定义一个字典digits,通过输入key，找到value
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]





reduce(fn,list(map(char2num,'13579')))

#map是针对字符串‘13579’中的每一个元素，生成一个匿名迭代器
#reduce(fn,Iterator)

'''
练习
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''


#capitalize() 将首字母大写，将其余的字母小写
def normalize(name):
    return name.capitalize()
L1=['Admin','sarah','yellOw']

#map先生成一个迭代器
#用list()生成一个list
L2=list(map(normalize,L1))




'''
    利用reduce进行乘积运算
'''
def prod(x,y):
    return  x*y
list1=[1,2,3,4,5]
reduce(prod,list1)


'''
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456：
'''


    
    
   

    
'''
    filter()函数--过滤序列
'''
def is_odd(n):
    return n%2==1
list(filter(is_odd,[1,2,4,5,6,7,8]))


#trip()--返回移除字符串头尾指定的字符生成的新字符串。




#定义一个生成器，生成无限的数字
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
        
def _not_visible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while(True):
        n=next(it)      #陈淑桦那个一个数字
        yield n
        it=filter(_not_visible(n),it)

for n in primes():
    if n<1000:
        print(n)
    else:
        break
    




#判断回文
def is_palindrome(n):
    nn=str(n)
    return nn==nn[::-1]

print(list(filter(is_palindrome,range(1000))))


'''

排序函数：sorted

'''
      
def by_name(t):
    return t[0].lower()
 
L=[('Bob',18),('Aracg',19)]
L1=sorted(L,key=by_name)
print(L1)

