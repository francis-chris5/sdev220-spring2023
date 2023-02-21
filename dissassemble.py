# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:20:59 2023

@author: franc

sdev 220 spring 2023
"""

import dis
import requests

    
def byRequest(blogpage):
    
    response = requests.get(blogpage)
    
    print(response.text)


if __name__=="__main__":

    dis.dis(byRequest("https://en.wikipedia.org/wiki/Python_(programming_language)"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
