# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:43:16 2023

@author: franc

sdev 220 spring 2023
"""



class Element():
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def display(self, head):
        if head == None:
            print("the list is empty")
        else:
            current = head
            while current != None:
                print(current.value)
                current = current.next
                

    def getElement(self, head, index):
        if head == None:
            print("noting in the list")
        else:
            counter = 0
            current = head
            while counter != index:
                current = current.next
                counter += 1
            return current.value





if __name__=="__main__":
    startingPoint = Element(3)
    startingPoint.next = Element(17)
    startingPoint.next.next = Element(29)
    
    startingPoint.display(startingPoint)
    print(startingPoint.getElement(startingPoint, 2 ))
    


























