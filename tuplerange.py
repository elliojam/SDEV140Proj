# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 18:28:32 2025

@author: ellio
"""

def myRange(start,end = None,step = None):
    """Creates a list starting at 'start', ending at 'end', increasing by 'step'"""
    # If 1 input is provided, it becomes the end, and start is zero
    if end == None and step == None:
        end = start
        start = 0
    
    # If step is not provided, default to 1
    if step == None:
        step = 1
       
    item = start
    mylist = []
    
    if step == 0:
        raise ValueError('step must not be zero')
        
    elif step > 0:
        while item <= end:
            mylist.append(item)
            item += step
            
    else: # if step < 0
        while item >= end:
            mylist.append(item)
            item += step
    
    return tuple(mylist)
