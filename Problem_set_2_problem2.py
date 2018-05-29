#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:58:29 2018

@author: tuheenahmmed
"""


 

'''

Problem 2 - Paying Debt Off in a Year

0.0/15.0 points (graded)

 

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.

By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

 

In this problem, we will not be dealing with a minimum monthly payment rate.

 

The following variables contain values as described below:

 

balance - the outstanding balance on the credit card

 

annualInterestRate - annual interest rate as a decimal

 

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

 

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

 

Monthly interest rate = (Annual interest rate) / 12.0

Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)

Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

 

 

                      Test Case 1:

                      balance = 3329

                      annualInterestRate = 0.2

 

                      Result Your Code Should Generate:

                      -------------------

                      Lowest Payment: 310

 

'''

'''

first version

 

'''
################

balance = 3329

annualInterestRate = 0.2

min_fixed_monthly_pay = 10
balance1=balance

          
while balance1 >0: 
    #print (balance)
    #print (balance1)

    balance1= balance
    
    min_fixed_monthly_pay+=10
    
    for month in range (1,13):
            
            
            monthly_unpaid_balance = balance1 - min_fixed_monthly_pay

            updated_monthly_balance = (monthly_unpaid_balance) + ((annualInterestRate/12.0) * monthly_unpaid_balance)

            updated_monthly_balance = round (updated_monthly_balance, 2)

            balance1 = updated_monthly_balance

                 
    #while balance1 < 0:

                #while monthly_unpaid_balance < 0:

                #print (monthly_unpaid_balance)

                #print (min_fixed_monthly_pay)

                #break 
    
    
#break
#print (monthly_unpaid_balance)
#print (min_fixed_monthly_pay)
print ('Lowest Payment: ' + str (min_fixed_monthly_pay))    

 
'''
#############
final and graded one
############
'''

balance = 3329

annualInterestRate = 0.2

min_fixed_monthly_pay = 10
balance1=balance

          
while balance1 >0: 

    balance1= balance
    
    min_fixed_monthly_pay+=10
    
    for month in range (1,13):
            
            
            monthly_unpaid_balance = balance1 - min_fixed_monthly_pay

            updated_monthly_balance = (monthly_unpaid_balance) + ((annualInterestRate/12.0) * monthly_unpaid_balance)

            updated_monthly_balance = round (updated_monthly_balance, 2)

            balance1 = updated_monthly_balance

                 
print ('Lowest Payment: ' + str (min_fixed_monthly_pay))    






 

 

 

 

 

 

 