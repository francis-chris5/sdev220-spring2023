# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:14:26 2023

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



############## binary file

import pickle

with open("datafile1.ppl", "wb") as toFile:
    pickle.dump(folks, toFile)
    

with open("datafile1.ppl", "rb") as fromFile:
    stuff = pickle.load(fromFile)
    print(stuff[3])




############## SQLite

import sqlite3 as sql

db = sql.connect("datafile2.db")

createQuery = "CREATE TABLE IF NOT EXISTS People(Name TEXT, Age INTEGER, Town TEXT);"

db.execute(createQuery)

for p in folks:
    insertQuery = "INSERT INTO People(Name, Age, Town) VALUES(\"" + p.name + "\", " + str(p.age) + ", \"" + p.town + "\");"
    cursor = db.execute(insertQuery)
    if cursor.rowcount >= 0:
        print("added the data")
    else:
        print("there was an error")
        
    
    
selectQuery = "SELECT name, age, town FROM People WHERE age >= 18;"


cursor = db.execute(selectQuery)
for row in cursor:
    print(row[0])
    
db.close()














###################################################