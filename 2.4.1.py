#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 03:55:07 2018

@author: tuheenahmmed
"""

def square(x):
    return x**2
 
    
    def square(x): 
        ans=x**2 
        print(ans)


###find a quadratic function
        

def evalQuadratic(a, b, c, x):
    
    a=float(a)
    b=float(b)
    c=float(c)
    x=float(x)
    
    ans = float(a*(x**2)+(b*x)+c)
    return ans

