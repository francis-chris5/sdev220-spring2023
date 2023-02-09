#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:36:11 2023

@author: chris
"""

from functools import wraps
import time


def double(x):
    return 2 * x


def sayHi():
    print("hola mundo")
    
#closure
def outer(x):
    print("getting ready to do other stuff")
    def inner():
        print("the other stuff")
        return
    inner()
    return x


#decorator
def signature(func):
    @wraps(func)
    def wrapping(*args, **kwargs):
        print("made by chris on 1/30")
        return func(*args, **kwargs)
    return wrapping
    
def timed(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time_ns()
        func(*args, **kwargs)
        end = time.time_ns()
        duration = end - start
        print(f"it took {duration} nanosecond to do that")
        return
    return


@signature
def triple(x):
    return x + x + x

@timed
def wasteOfTime():
    for i in range(10000):
        x = i * 2
    

if __name__ == "__main__":
    x = double(3)
    y = sayHi()
    
    print(x, y)
    
    outer(5)
    
    print(triple(4))


    #print(wasteOfTime())


















###########  white spac
