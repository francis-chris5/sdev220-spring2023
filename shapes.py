# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:21:35 2023

@author: franc

sdev 220 spring 2023
"""

import abc ## abstract base class
import math

## abstract class
class Shape(metaclass=abc.ABCMeta):
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def getArea(self):
        return
    
    
    def __eq__(self, other):
        if self.getArea() == other.getArea():
            return True
        else:
            return False
        
    def __repr__(self):
        return "the area is " + str(self.getArea())


## concrete classes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getArea(self):
        return self.length*self.width
    
   
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
       
    def getArea(self):
        return self.radius**2 * math.pi
    
    

    
if __name__=="__main__":
    r = Rectangle(3, 4)
    s = Rectangle(2, 6)
    t = Rectangle(3, 3)
    
    if r == s:
        print("those are the same")
    else:
        print("those don't match")
        
    if r == t:
        print("those are the same")
    else:
        print("those don't match")
    print(r)
    
    for i in range(12):
        c = Circle(i)
        print(c)
    
    
    




























###################################