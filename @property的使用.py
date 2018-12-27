# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:18:14 2018

@author: Lucy


CRTL+i 查看方法的具体细节
"""


'''
    @property的实现比较复杂，我们先考察如何使用。
    把一个getter方法变成属性，只需要加上@property就可以了，
    @score.setter()表示变成一个score.set_score()方法
'''
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    '''
        还可以定义只读属性，只定义getter方法，
        不定义setter方法就是一个只读属性：
    '''
    @property      #相当于get_birth(self)方法
    def birth(self):
        return self._birth

    @birth.setter  #相当于set_birth(self)方法
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

    
    '''
        上面的birth是可读写属性，
        而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
    '''
   
    
class Screen(object):
      @property
      def width(self):
         return self._width
     
      @width.setter
      def width(self,value):
          self._width=value
          
      @property
      def height(self):
          return self._height
      
      @height.setter
      def height(self,value):
          self._height=value
          
      @property 
      def resolution(self):
         return (self._height)+(self._width)
          
      
    
        
    
     
    

