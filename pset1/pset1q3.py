#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order. For 
example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

def find_longest_substring_in_alphabetical_order(s):
    groups = []
    cur_longest = ''
    prev_char = '' # this equals to 0
    for i in range(0, len(s)):
        if prev_char and s[i] < prev_char:
            groups.append(cur_longest)
            cur_longest = s[i]
        else:
            cur_longest += s[i] # concatenate
        # if reached end of string, next if statement will not be executed.
        # Add this guard statement to check in case the last n letters are longest
        if (i == len(s)-1 and s[i] > prev_char):
           groups.append(cur_longest)
        prev_char = s[i]
    return max(groups, key=len) if groups else s

s = 'eycstpipqz' # test vector

count = find_longest_substring_in_alphabetical_order(s)
print ("Longest substring in alphabetical order is:", count)