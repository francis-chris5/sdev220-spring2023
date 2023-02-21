# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:11:34 2023

@author: franc

sdev 220 spring 2023
"""



class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        item = self.stack[-1]
        self.stack.remove(item)
        return item
    
    
    
if __name__=="__main__":
    s = Stack()
    s.push(3)
    s.push(17)
    s.push(29)
    
    print(s.stack)
    
    print(s.pop())
    print(s.stack)
    
    












