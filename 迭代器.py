# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:04:33 2018

@author: Lucy
"""

#迭代对象 Iterable
#迭代器：Iterator
#next()函数调用并不断返回下一个值的对象称为迭代器：Iterator,
    #所以Iterator就是一个Iterable对象
    
from collections import Iterator
isinstance((x for x in range(10)),Iterator)
isinstance([],Iterator)

#str,list,dict都不是一个Iterator
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
#而使用list是永远不可能存储全体自然数的。
#通过一个iter()函数获得一个Iterator对象

L=[1,2,3,4]
M=iter(L)
isinstance(M,Iterator)