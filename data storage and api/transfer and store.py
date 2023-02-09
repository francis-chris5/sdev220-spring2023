# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:30:53 2023

@author: franc

sdev 220 spring 2023
"""


from people import Person

folks = [
    Person("Sally", 34, "Salem"),
    Person("Charlie", 28, "Charlestown"),
    Person("Corey", 16, "Corydon"),
    Person("Lewie", 73, "Louisiville"),
    Person("Jeffery", 14, "Jeffersonville")
    ]


#########################  csv

import csv

with open("datafile3.csv", "w") as toFile:
    writer = csv.writer(toFile)
    for f in folks:
        writer.writerow([f.name, f.age, f.town])

with open("datafile3.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) != 0:
            print(row)



######################## JSON

import json

with open("datafile4.json", "w") as toFile:
    for f in folks:
        toFile.write(json.dumps({"name": f.name, "age": f.age, "town": f.town}) + "\n")
        

with open("datafile4.json") as fromFile:
    for line in fromFile:
        print(json.loads(line.strip()))
        
    
############################ XML


nicknames = ["sal", "chuck", "beanstalk", "double-l", "Big-J"]

import xml.etree.ElementTree as et


root = et.Element("People")
for count, f in enumerate(folks):
    branch = et.SubElement(root, "person")
    
    leaf1 = et.SubElement(branch, "name")
    leaf1.text = f.name
    leaf1.attrib = {"nickname": nicknames[count]}
    
    
    leaf2 = et.SubElement(branch, "age")
    leaf2.text = str(f.age)
    
    leaf3 = et.SubElement(branch, "town")
    leaf3.text = f.town

tree = et.ElementTree(root)

with open("datafile5.xml", "wb") as toFile:
    tree.write(toFile)
    

newTree = et.parse("datafile5.xml")


    
newRoot = newTree.getroot()

for i in range(len(newRoot)):
    for j in range(len(newRoot[i])):
        print(newRoot[i][j].tag + " : " + newRoot[i][j].text)
        print(newRoot[i][j].attrib)























#################################################