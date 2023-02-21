# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:27:56 2023

@author: franc

sdev 220 spring 2023
"""



class Queue():
    def __init__(self):
        self.queue = []
        
    
    def poll(self, value):
        self.queue.insert(0, value)
        
    def remove(self):
        item = self.queue[-1]
        self.queue.remove(item)
        return item
    
    
if __name__=="__main__":
    q = Queue()
    q.poll(3)
    q.poll(17)
    q.poll(29)
    
    
    print(q.queue)
    
    print(q.remove())
    
    print(q.queue)
    
        































