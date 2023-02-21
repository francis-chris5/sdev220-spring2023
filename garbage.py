# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:49:04 2023

@author: franc

sdev 220 spring 2023
"""

import gc


x = 12
y = 5

print(x + y)

del x

gc.collect()
