# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:34:24 2023

@author: franc

sdev 220 spring 2023
"""



import multiprocessing as mp

import random

asyncResults = [] ##must have a place to put the pieces
def collectResults(res):
    asyncResults.append(res)

def adding(arr):
    s = 0
    for a in arr:
        s += a
    return s



    


if __name__ == "__main__":
    cores = mp.Pool(mp.cpu_count())

    data = []
    for i in range(25):
        data.append(random.random())
        
    print()
    print()
    print()
    
    ## synchronously
    
    syncResult = cores.apply(adding, args=[data])
    print(syncResult)
    mapResult = cores.map(adding, [data])
    print(mapResult)
        
        
    ## asyncrhonously
    
    cores.apply_async(adding, args=[data], callback=collectResults)
    
# =============================================================================
#     Do OTHER STUFF HERE
# =============================================================================
    cores.close()
    cores.join()
    
    print(asyncResults)



















