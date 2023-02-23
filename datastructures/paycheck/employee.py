# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:53:55 2023

@author: franc

sdev 220 spring 2023
"""



class Employee():
    def __init__(self, name, age, town, empID, payRate, deductions):
        self.name = name
        self.age = int(age)
        self.town = town
        self.empID = empID
        self.payRate = float(payRate)
        self.deductions = float(deductions)
        self.next = None
        
    def pay(self, hours):
        if hours < 40:
            gross = hours * self.payRate 
        else:
            gross = 40 * self.payRate + (hours - 40) * self.payRate * 1.5
        withholding = gross * self.deductions
        net = gross - withholding
        return self.name, gross, withholding, net
    
    
    def push(self, head, empl):
        if head.next == None:
            head.next = empl
        else:
            self.push(head.next, empl)
            
           
            
    def pop(self, head):
        if head.next.next == None:
            top = head.next
            head.next = None
            hours = float(input(f"how many hours did {self.name} worked this week: "))
            return top.pay(hours)
        else:
            self.pop(head.next)
            
            
        
        
















        
    
        
    