# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:53:55 2023

@author: franc

sdev 220 spring 2023
"""

import csv


class Employee():
    def __init__(self, name, age, town, empID, payRate, deductions):
        self.name = name
        self.age = int(age)
        self.town = town
        self.empID = empID
        self.payRate = float(payRate)
        self.deductions = float(deductions)
        self.next = None
        self.hours = []
        self.counter = 0
        
    def pay(self, hours):
        #print(f"calculating for {self.name} with {hours} hours at {self.payRate}")
        if hours < 40:
            gross = hours * self.payRate      
        else:
            gross = 40 * self.payRate + (hours - 40) * self.payRate * 1.5
        withholding = gross * self.deductions
        net = gross - withholding
        ## print(f"gross pay is {gross}")
        ## print(f"withholding is {withholding}")
        ## print(f"net pay is {net}")
        return self.empID, self.name, gross, withholding, net
    
    
    def push(self, head, empl):
        if head.next == None:
            head.next = empl
        else:
            self.push(head.next, empl)
            
           
            
    def pop(self, head):
        if head.next.next == None:
            top = head.next
            head.next = None
            ## corrected which name shows in input method
            #hours = float(input(f"how many hours did {top.name} worked this week: "))
            self.counter -= 1
            return top.pay(float(self.hours[self.counter]))
        else:
            return self.pop(head.next) ## THIS WAS THE PROBLEM, FORGOT TO RETURN
            
    ## copied over the display method from list we made mondy, stack checks out      
    def display(self, head):
        if head == None:
            print("the list is empty")
        else:
            current = head
            while current != None:
                print(current.name)
                current = current.next
    
            
    
    def getHours(self, filename):
        with open(filename, "r") as fromFile:
            reader = csv.reader(fromFile)
            for line in reader:
                if len(line) != 0:
                    self.hours = line
                    self.counter = len(self.hours)
















        
    
        
    