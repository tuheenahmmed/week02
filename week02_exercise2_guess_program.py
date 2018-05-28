# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:16:20 2018

@author: etuhahm
"""
'''
In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
Here is a transcript of an example session:
    

    Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 25?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 37?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 43?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 40?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 41?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 42?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 42

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 93?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 90?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 91

'''

@@@@@@@@@@@@@ version 01  @@@@@@@@@@@@@@@@@@@@@

guess= int(input("Type an integer between 0 (inclusive) and 100 (not inclusive): ")) 
  
x = 100
epsilon = 1
numGuesses = 0

low = 0
high = x
ans = (high + low)/2

while abs(ans - guess) >= epsilon:
    numGuesses += 1
    if ans < guess :
        
        text1 = input("enter 'l' to indicate the guess is too low: ")
        low=ans
        ans = int((high + low)/2)  
        print (ans)
    elif ans > guess:
             
        text2 = input("enter 'h' to indicate the guess is too high: ")
        high=ans
        ans = int((high + low)/2)  
        print (ans)
    elif ans == guess:
                 
        text3 = input("enter 'c' to indicate the guess is right: ")
        ans = int((high + low)/2)     
        print (ans)

print('numGuesses = ' + str(numGuesses))
print ("Game Over Your secret number was: "+ str(ans))



    
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  version 02
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
print ("Please think of a number between 0 and 100!") 
  
x = 100
epsilon = 1
numGuesses = 0

low = 0
high = x
ans = int((high + low)/2)

while abs(ans - high) >= epsilon:
    
    print ("Is your secret number "+ str(ans)+"?")
    text1 = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

#if text1 != 'h' or text1 != 'l' or text1 != c:
#print ("Sorry, I did not understand your input.")   

    if text1 == 'l':
        
            numGuesses += 1
            low=ans
            ans = int((high + low)/2)  
            print (ans)
    
    elif text1 == 'h':
             
            high=ans
            ans = int((high + low)/2)  
            print (ans)
    
    elif text1 == 'c':
            break
                 
print('numGuesses = ' + str(numGuesses))
print ("Game Over Your secret number was: "+ str(ans))



$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$final one$$$$$$$$$$$$$$$$$$$$$

print ("Please think of a number between 0 and 100!") 
  
x = 100
epsilon = 1
numGuesses = 0

low = 0
high = x
ans = int((high + low)/2)

while abs(ans - high) >= epsilon:
    numGuesses += 1
    
    print ("Is your secret number "+ str(ans)+"?")
    text1 = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    print (text1)
    while text1 != 'h' and text1 != 'l' and text1 != 'c':
        print ("Sorry, I did not understand your input.")   
        break 
          
    if text1 == 'l':
                            
                    low=ans
                    ans = int((high + low)/2)  
                    #print (ans)
    
    elif text1 == 'h':
             
                    high=ans
                    ans = int((high + low)/2)  
                    #print (ans)
            
    elif text1 == 'c':
                    break
                         
#print('numGuesses = ' + str(numGuesses))
print ("Game Over Your secret number was: "+ str(ans))



^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^final version and graded one ^^^^^^^^^^^^^^^^^^^^
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print ("Please think of a number between 0 and 100!") 
  
x = 100
epsilon = 1
numGuesses = 0

low = 0
high = x
ans = int((high + low)/2)

while abs(ans - high) >= epsilon:
    numGuesses += 1
    
    print ("Is your secret number "+ str(ans)+"?")
    text1 = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #print (str(text1))
  
    while str(text1) != 'h' and str(text1) != 'l' and str(text1) != 'c':
        #print (str(text1))
        print ("Sorry, I did not understand your input.")   
        break 
          
    if text1 == 'l':
                            
                    low=ans
                    ans = int((high + low)/2)  
                    #print (ans)
    
    elif text1 == 'h':
             
                    high=ans
                    ans = int((high + low)/2)  
                    #print (ans)
            
    elif text1 == 'c':
                    break
                         
#print('numGuesses = ' + str(numGuesses))
print ("Game Over Your secret number was: "+ str(ans))

























