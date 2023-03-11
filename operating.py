# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:35:16 2023

@author: franc

sdev 220 spring 2023
"""


from os import makedirs, rmdir, listdir, getcwd, system
from os.path import isdir, isfile, join


path = getcwd()


for thing in listdir():
    if isdir(join(path, thing)):
        print("folder")
        for f in listdir(join(path, thing)):
            print("\t\t" + f)
    else:
        print("file: " + thing)
            

if not isdir(join(path, "tivquestion")):
    makedirs("tivquestion")
with open("tivquestion/greeting.py", "w") as toFile:
    toFile.write("print(\"Hello World\")")


exec(open("tivquestion/greeting.py").read())
            

##os.system

system("python tivquestion/greeting.py")


















