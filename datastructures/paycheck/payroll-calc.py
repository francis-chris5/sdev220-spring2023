# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:47:05 2023

@author: franc

sdev 220 spring 2023
"""

from employee import Employee
import csv

boss = Employee("bossman", 40, "hometown", 0000, 0.00, 0)

with  open("workforce.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) != 0:
            tmep = Employee(row[0], row[1], row[2], row[3], row[4], row[5])
            boss.push(boss, tmep)
            
            
while boss != None:
    print(boss.pop(boss))
    