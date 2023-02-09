# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:47:17 2023

@author: franc

sdev 220 spring 2023
"""



import math

def piDigits():
    p = str(math.pi)
    i = 0
    while i < len(p):
        if p[i].isnumeric():
            yield int(p[i])
        i += 1
        
if __name__=="__main__":
    
    for i in piDigits():
        j = 0
        line = ""
        while j < i:
            line += "*"
            j += 1
        print(line)
        

    counter = 0
    for i in piDigits():
        counter += 1
        if i == 7:
            print(counter)




























################################ white space 

