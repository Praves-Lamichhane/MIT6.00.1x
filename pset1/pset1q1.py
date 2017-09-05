#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print: 
    
    Number of vowels: 5
"""

s = 'azcbobobegghakl' # sample test data
vowel_set = ['a', 'e', 'i', 'o', 'u'] # define vowel set.

count = 0;
for c in s:
    if c in vowel_set:
        count = count + 1;

print ("Number of vowels: ", count);