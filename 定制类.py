# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:19:45 2018

@author: Lucy
"""

'''
    __str__
    
'''
class Student(object):
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    
    __repr__=__str__
    
    
'''
    怎么才能打印得好看呢？
    只需要定义好__str__()方法，返回一个好看的字符串就可以了：
'''
s=Student('Michael')




'''
    __iter__
    
    如果一个类想被用于for ... in循环，类似list或tuple那样，
    就必须实现一个__iter__()方法，该方法返回一个迭代对象，
    然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    直到遇到StopIteration错误时退出循环。
        
'''

class  Fib(object):
    def __init__(self):
        self .a,self.b=0,1
    
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration()
        return self.a
    
    #表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    #现在，就可以按下标访问数列的任意一项了
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
    
    #实现类似List的切片操作
    '''
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append[a]
                a,b=b,a+b
            return L
    '''
    
    
    '''
        当类的属性不存在，但是还是调用的时候，使用 __getattr__
    '''
    def __getattr__(self,attr):
        if attr=='score':
            return 99
        #不存在score属性，此时默认值是99，并发出警报，说明Student类没有改属性
        raise AttributeError('\'Student object has no attribute\'%s\'' % attr)
        


#定义一个Student  
class Student(object):
    def __init__(self,name):
        self.name=name
        
    '''
        一个对象实例可以有自己的属性和方法，当我们调用实例方法时，
        我们用instance.method()来调用。能不能直接在实例本身上调用呢？
        在Python中，答案是肯定的
    '''
    def __call__(self):
        print('MY name is %s' %self .name)
    
s=Student('Michael')


'''
    怎么判断一个变对象是能被调用？---使用Callable()
'''

