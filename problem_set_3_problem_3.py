#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 04:08:26 2018

@author: tuheenahmmed


while bal isnt close enough to zero:
  do your 12 month calculation for latest payment value
  if    higher
  elif  lower
  no else so it will be tested and ok at top of loop
  
  
  Hopefully this isn't spoiling too much. I initially started my while loop basically this way:

while the abs(balance - the payment * 12) is greater than .01:
The results I was getting were too small. This was early in my tries so it may've been a million other issues but 
I figured at the time that it was because that while condition didn't take into account the interest that gets added 
onto the balance as it's paid off. Switching it the balance figure to balance + maxInterest didn't seem right to me either, 
because theoretically we shouldn't be paying that much interest (we're paying monthly).

While True

print("Lowest: {:0.2f}".format(payment)) 

while abs(unpaid_balance)>0.01

"""

balance = 3329
annualInterestRate = 0.2


monthly_interest_rate = (annualInterestRate)/12.0
monthly_lower_bound = balance/12.0
monthly_upper_bound = (balance * (1+monthly_interest_rate)**12)/12.0

min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0
x= balance+monthly_upper_bound 

epsilon = .01

while balance1 != +.01 or -.01:
    
        balance1=balance

        for month in range (1,13):

            monthly_unpaid_balance = balance1 - min_fixed_monthly_pay
            updated_monthly_balance = (monthly_unpaid_balance) + ((annualInterestRate/12.0) * monthly_unpaid_balance)
            updated_monthly_balance = round (updated_monthly_balance, 2)
            balance1 = updated_monthly_balance


        if (min_fixed_monthly_pay*12) < balance:

            monthly_lower_bound = min_fixed_monthly_pay

        else:

            monthly_upper_bound = min_fixed_monthly_pay

   
        min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0


print ('Lowest Payment: ' + str (min_fixed_monthly_pay)) 



'''

********second try*********
'''

balance = 3329
annualInterestRate = 0.2


monthly_interest_rate = (annualInterestRate)/12.0
monthly_lower_bound = balance/12.0
monthly_upper_bound = (balance * (1+monthly_interest_rate)**12)/12.0

min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0

balance1=balance

epsilon = .01

while abs(balance1) != .01:
    
        balance1=balance
        

        for month in range (1,13):

            monthly_unpaid_balance = balance1 - min_fixed_monthly_pay
            updated_monthly_balance = (monthly_unpaid_balance) + ((annualInterestRate/12.0) * monthly_unpaid_balance)
            balance1 = updated_monthly_balance

        balance1 = round (balance1, 2)
        
        if balance1>0 :
            print (balance1) 
            monthly_lower_bound = min_fixed_monthly_pay

        else:

            monthly_upper_bound = min_fixed_monthly_pay

   
        min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0


#print ('Lowest Payment: ' + str (min_fixed_monthly_pay)) 
print("Lowest Payment: {:0.2f}".format(min_fixed_monthly_pay))


'''
final and graded one
got 20/20
Tokyo, Japan
'''

balance = 320000
annualInterestRate = 0.2


monthly_interest_rate = (annualInterestRate)/12.0
monthly_lower_bound = balance/12.0
monthly_upper_bound = (balance * (1+monthly_interest_rate)**12)/12.0

min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0

balance1=balance

epsilon = .01

while abs(balance1) != .01:
#while True:
    
        balance1=balance
        

        for month in range (1,13):

            monthly_unpaid_balance = balance1 - min_fixed_monthly_pay
            updated_monthly_balance = (monthly_unpaid_balance) + ((annualInterestRate/12.0) * monthly_unpaid_balance)
            balance1 = updated_monthly_balance

        balance1 = round (balance1, 2)
        #print (balance1) 
        
        if monthly_unpaid_balance > 0:
            
            monthly_lower_bound = min_fixed_monthly_pay

        else:

            monthly_upper_bound = min_fixed_monthly_pay

   
        min_fixed_monthly_pay = (monthly_lower_bound+monthly_upper_bound)/2.0


#print ('Lowest Payment: ' + str (min_fixed_monthly_pay)) 
print("Lowest Payment: {:0.2f}".format(min_fixed_monthly_pay))




