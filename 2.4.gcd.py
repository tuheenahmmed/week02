#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:31:39 2018

@author: tuheenahmmed
"""
"""
ESTIMATED TIME TO COMPLETE: 5 minutes

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. 
For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, 
and iteratively reduce this test value by 1 until you either reach a case 
where the test divides both a and b without remainder, or you reach 1.
"""




def gcdIter(a, b):
    
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a < b:
        
        test = a 
    
    else:
    
        test = b
           
    
    for test in range (test,0, -1):
        
        if b%test == 0 and a%test ==0:  
             
            return test
    
    
print (gcdIter (11,17))
        
        




