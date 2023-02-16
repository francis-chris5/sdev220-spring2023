# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:14:09 2023

@author: franc

sdev 220 spring 2023
"""

class Person():
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.age == other.age)
        
    def __repr__(self):
        return f"{self.name} is {self.age} years old and lives in {self.town}."