#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times 
the string 'bob' occurs in s. For example, if 
s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""

def count_substring(string, sub_string):

    length = len(string)
    counter = 0
    for i in range(length): # locked down the position
        for j in range(length):
            if string[i:j+1] == sub_string: # seek up the substring
                counter +=1
    return counter

s = 'azcbobobegghakl' # sample test data
count = count_substring(s, "bob")
print ("Number of times bob occurs is: ", count);

