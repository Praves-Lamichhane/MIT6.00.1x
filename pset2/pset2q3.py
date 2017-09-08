#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. 
Why did we make it that way? You can try running your code locally so that the 
payment can be any dollar and cent amount (in other words, the monthly payment is 
a multiple of $0.01). Does your code still work? It should, but you may notice 
that your code runs more slowly, especially in cases with very large balances 
and interest rates. (Note: when your code is running on our servers, there are 
limits on the amount of computing time each submission is allowed, so your 
observations from running this experiment on the grading system might be 
limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did 
in Problem 2 without running into the problem of slow code? We can make this 
program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

1. balance - the outstanding balance on the credit card

2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that 
we can pay off the entire balance within a year. What is a reasonable lower bound 
for this payment value? $0 is the obvious anwer, but you can do better than that. 
If there was no interest, the debt can be paid off by monthly payments of one-twelfth 
of the original balance, so we must pay at least this much every month. One-twelfth 
of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the 
entire balance at the end of the year. What we ultimately pay must be greater than 
what we would've paid in monthly installments, because the interest was compounded 
on the balance we didn't pay off each month. So a good upper bound for the monthly 
payment would be one-twelfth of the balance, after having its interest compounded 
monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out 
the Wikipedia page on bisection search) to find the smallest monthly payment to the 
cent (no more multiples of $10) such that we can pay off the debt within a year. 
Try it out with large inputs, and notice how fast it is (try the same large inputs 
in your solution to Problem 2 to compare!). Produce the same return value as you 
did in Problem 2.

"""
EPSILON = 0.01; # precision



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

# bisection search
def calculate_minimum_payment_bisearch (balance, annualInterestRate):    
    monthly_interest_rate = annualInterestRate/12;
    lower_bound_monthly_payment = balance/12;
    upper_bound_monthly_payment = (balance * (1+monthly_interest_rate)**12)/12;
    
    # stop condition
    while (upper_bound_monthly_payment - lower_bound_monthly_payment > EPSILON):
        # calculate mid-point
        midpoint_payment = (lower_bound_monthly_payment + upper_bound_monthly_payment)/2;
        # if f(a) and f(mid) has the same sign
        if (calculate_balance(balance, annualInterestRate, lower_bound_monthly_payment) 
           *calculate_balance(balance, annualInterestRate, midpoint_payment) > 0):
            # too far away (not ensuring f(a) and f(mid) is in different sign), move closer..
            lower_bound_monthly_payment = midpoint_payment;
        else:
            # yes, on the right track, moving closer..
            upper_bound_monthly_payment = midpoint_payment;
    return midpoint_payment;
    

# Example test vector
balance = 999999;
annualInterestRate = 0.18;

# test = calculate_balance(balance, annualInterestRate, 29157.09);
min_payment = calculate_minimum_payment_bisearch(balance, annualInterestRate);
print("Lowest Payment: %.2f" %min_payment);




