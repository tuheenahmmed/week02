#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 09:58:04 2018

@author: tuheenahmmed
"""


The natural exponential function y = ex
In mathematics, an exponential function is a function of the form f(x) = b to the power x


Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. 
For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer  0. 
It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$ ITERATIVE $$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

''
2 x 1
2 x 2
2 x 3
2 x 4
2 x 5



def iterPower(base, exp):
    
    if exp >= 0:
        
        for i in range (1, exp+1):
        
        my_exponential = base * exp * (exp - i)
        
        print (str(prod))
        
        return prod
    
    else:
        break
    
print (iterPower (2, 5))


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$ RECURSIVE $$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    ''
    = 2
    = 2 x 2
    = 2 x 2 x 2
    ''

def iterPower(base, exp):
    
    
    prod = 1
    
    for i in range (1, exp+1):
        
        prod *= base
        print (str(prod))
        
    return prod


print (iterPower (2, 5))