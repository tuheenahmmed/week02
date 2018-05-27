#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:12:20 2018

@author: tuheenahmmed
"""

"""
Exercise: is in
0.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 18 minutes

We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. 
If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. 
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. 
char will be a single character and aStr will be a string that is in alphabetical order. 
The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    
    
    Hints
    Basic function structuring
    Be very careful about how you slice the string in the recursive cases! 
    Before you execute the recursive cases, you test the middle character - 
    so if you reach the recursive cases, you know the middle character cannot be a match, right? 
    So be careful to not include this character when you make your recursive call!

    What should your base case be?
        You should be thinking about 3 situations:
            1. What happens when the string is empty?

            2. What happens when the string is of length 1?

            3. What happens when the test character equals the middle character?

    What should your recursive case be?
    You should be thinking about 2 situations:
            1. What happens when the test character is smaller than the middle character?
            2. What happens when it is larger?

    '''
    # Your code here
    
    #aStr = 'abcdef'
    #char = 'a'
    

    if len(aStr) == 0:
        
        return False
    
    if len(aStr) == 1:
        
        return False
    
    
    middle = int(len(aStr) / 2)
    
    #print (aStr[middle])
    
    '''
    can combine first two if statements
    '''
    
    if char == aStr[middle]:
        
        return True
    
    else:
        
        if char < aStr[middle]:
            
            return isIn (char, aStr[:middle])
        else:
            
            return isIn (char, aStr[middle:])

print (isIn('c', 'abcdefghijk'))




$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
final one
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) == 0 or len(aStr) == 1:
        
        return False
        
    
    middle = int(len(aStr) / 2)
    
    
    if char == aStr[middle]:
        
        return True
    
    else:
        
        if char < aStr[middle]:
            
            return isIn (char, aStr[:middle])
        else:
            
            return isIn (char, aStr[middle:])

print (isIn('c', 'abcdefghijk'))



