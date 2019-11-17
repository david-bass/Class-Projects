#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:05:52 2018

@author: davidbass
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

print('Test 1')

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
    
print('Test 3')

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
print('Test 4')

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
print('Test 5')

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
print('PROBLEM 1')

s = ('This is a test of uniform maddness')
vowel_count = 0
for v in s:
    if(v == str('a') or v==str('e') or v==str('i') or v==str('o') or v==str('u')):
        vowel_count += 1
#    vowel_count += 1
        
print ('Number of vowels: ' + str(vowel_count))

print('PROBLEM 2')

s = ('This is a test bob of uniform bobob maddness')
bob_count = 0
for b in range(len(s)):
    if s[b:b+3] == 'bob':
        bob_count += 1

print("Number of times bob occurs is: " + str(bob_count))

print('Problem 3')

s = ('abcdaefghiajkracadabrarstxyz')
count = ''
count2 = ''
#iterate over s for the total length
for i in range(len(s)):
    # compare current iteration to prior, and if less than then add to count
    if (s[i] >= s[i-1]):
        count += s[i]
    else:
        count = (s[i]) # If not, then count starts over
    if len(count) > len(count2):  #compare count to count2
        count2 = count   #if count is greater than count2, then count is stored in counts2
        # count2 stores the longest string

print("Longest substring in alphabetical order is: " + str(count2))
