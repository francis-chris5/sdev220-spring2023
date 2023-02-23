# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:28:51 2023

@author: franc

sdev 220 spring 2023
"""



from employee import Employee
import csv


x = input("is there another employee (yes/no): ")
while x.lower() == "yes":
    name = input("enter name: ")
    age = int(input("enter age: "))
    town = input("enter town: ")
    empID = input("enter last four digits of social: ")
    rate = float(input("enter the rate of pay: "))
    deductions = float(input("enter the percentage of witholdings (as percent): ")) / 100
    with open("workforce.csv", "a") as toFile:
        writer = csv.writer(toFile)
        writer.writerow([name, age, town, empID, rate, deductions])
    x = input("is there another employee (yes/no): ")

























    