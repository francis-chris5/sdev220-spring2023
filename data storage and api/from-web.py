# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:18:00 2023

@author: franc

sdev 220 spring 2023
"""


import urllib
import requests

def byURL():
    blogpage = "http://csfrancis555.com/blogs/climate.php"
    
    webhandler = urllib.request.urlopen(blogpage)
    
    contents = webhandler.read()
    
    print(contents)
    

def byRequest(blogpage):
    
    response = requests.get(blogpage)
    
    print(response.text)
    
    






if __name__ == "__main__":
    byURL()
    print()
    print()
    print()
    byRequest("http://csfrancis555.com/blogs/climate.php")
    byRequest("https://en.wikipedia.org/wiki/Python_(programming_language)")














#################