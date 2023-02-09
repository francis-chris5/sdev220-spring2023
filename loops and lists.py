#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:28:59 2023

@author: chris
"""

import functions


print(double(5))


i = 0
while i < 12:
    print(f"the next number is {i}")
    i += 1
    

print()
print()

for i in range(12):
    print(f"the next number is {i}")
    


myList = [3, 14, 87, 2, 9, 5]

print(myList[1] / myList[4])

for item in myList:
    print(item)
    

triples = []
for i in range(100):
    if i % 3 == 0:
        triples.append(i)
        
        
#list comprehension
threes = [t for t in range(100) if t%3==0]


#generator comprehension
for i in (t for t in range(100) if t%3==0):
    print(i)




















########## white space 
