#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but 
instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year, for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at 
the end of the month (after the payment for that month is made). The monthly 
payment must be a multiple of $10 and is the same for all months. Notice 
that it is possible for the balance to become negative using this payment 
scheme, which is okay. 

"""

# Monthly interest rate= (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + 
#                              (Monthly interest rate x Monthly unpaid balance)

# helper function to calculate the balance over 12 months with fixed monthly payment
def calculate_balance (balance, annualInterestRate, fixed_monthly_payment):
    number_of_months = 12; # 1 year = 12 months
    monthly_interest_rate = annualInterestRate/12;
    prev_balance = balance; # initially
    for month in range(0,number_of_months):
        monthly_unpaid_balance = prev_balance - fixed_monthly_payment;
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate*monthly_unpaid_balance);
        prev_balance = updated_balance;        
    return updated_balance;

def calculate_minimum_payment (balance, annualInterestRate):
    
    minimum_monthly_payment = 0; # initial guess
    while True:
        curr_balance = calculate_balance(balance, annualInterestRate, minimum_monthly_payment);
        if (curr_balance < 0): # paid off the card
            return minimum_monthly_payment;
        else:
            minimum_monthly_payment += 10; # increment the guess value
    return minimum_monthly_payment;


# Example test vector
balance = 3329;
annualInterestRate = 0.2;

min_payment = calculate_minimum_payment(balance, annualInterestRate);
print("Lowest Payment: %d" %min_payment);
