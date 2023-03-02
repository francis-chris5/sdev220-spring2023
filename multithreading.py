# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:15:13 2023

@author: franc

sdev 220 spring 2023
"""

import threading

## make sure x is > 0
def busywork(x):
    while x > 0:
        print(f"just doing some random stuff, pass number {x}")
        x -= 1
        
        
## make sure y is really big
def tediouswork(y):
    while y > 12:
        print(f"carrying out a heavy load here, pass number {y-12}")
        y -= 1
        


if __name__=="__main__":
    firstthread = threading.Thread(target=busywork, args=(18,))
    secondthread = threading.Thread(target=tediouswork, args=(25,))
    
    
    firstthread.start()
    secondthread.start()
    
    firstthread.join()
    secondthread.join()
    
    print("--------------  ALL DONE  -------------")
    

    























