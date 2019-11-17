#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:28:10 2018

@author: davidbass
"""

#iteration = 0
#count = 0
#while iteration < 5:
#    # the variable 'letter' in the loop stands for every 
#    # character, including spaces and commas!
#    for letter in "hello, world": 
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#    
#iteration = 0
#
#while iteration < 5:
#    # the variable 'letter' in the loop stands for every 
#    # character, including spaces and commas!
#    count = 0
#    for letter in "hello, world": 
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#    
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#        if iteration % 2 == 0:
#            break
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#    
#print('question 1')
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) < epsilon:
#        break
#    else:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))
# 
#print('question 2')    
##x = 25
##epsilon = 0.01
##step = 0.1
##guess = 0.0
#
##while guess <= x:
##    if abs(guess**2 -x) >= epsilon:
# #       guess += step
#
##if abs(guess**2 - x) >= epsilon:
##    print('failed')
##else:
##    print('succeeded: ' + str(guess))
#  
#print('question 3')  
#x = 23
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while abs(guess**2-x) >= epsilon:
#    if guess <= x:
#        guess += step
#    else:
#        break
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))
#    
#print('Exercise: guess my number')
#
#
#high = 100
#low = 0
#guessed = False
#print('Please think of a number between 0 and 100!')
#
#while not guessed:
#    guess = (high + low)//2
#    print("Is your secret number " + str(guess)+ "?")
#    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
#    if user_inp == 'c':
#        guessed = True
#    elif user_inp == 'h':
#        high = guess
#    elif user_inp == 'l':
#        low = guess
#    else:
#        print("Sorry, I did not understand your input.")
#        
#print('Game over, your number is:' + str(guess))



x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print ('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p +=1
    
num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
    
for i in range(p - len(result)):
    result = '0' + result
    
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + " is " + result)
"""
"""
def is_even(i):
    '''
    Input: i, a positive integer
    Returns True if i is even, otherwise returns False
    '''
    print('hi')
    return i%2 == 0

def square(x):
    '''
    x: int or float.
    '''
    return x*x
    return square(square(x))

def f(y):
    x = 1
    x += 1
    print(x)
    
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
g(x)
print(x)

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x -', x)
    h()
    return x

x = 3
z = g(x)

def recurPower1(base, exp):
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)
    
    
    
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(4, 'P1', 'P2', 'P3'))

print("Exercise GCD Iter")
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = a
    
    while a % gcd != 0 or b % gcd !=0:
            gcd -= 1
    return gcd

print(gcdIter(15, 18))


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    return gcdRecur(b, a % b)

print(gcdRecur(15, 18))

print('Video of Fibonacci')
def fib(x):
    """ assumes x and int >= 0
    returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(6))

print('Video: Recursion on non-numerics')
# palindrome program to determine if one or not

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

print(isPalindrome('sas'))


print('Exercise: Is In')

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #Check if zero characters
    if len(aStr) == 0:
        return False
    # check if only 1 character and if they match.  If so then return true
    if len(aStr) == 1 and char == aStr:
        return True
    #bisection search against aStr to test and eliminate section of aStr
    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    #check first half recursively
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    #check bottom half if char is greater than midIndex
    else:
        return isIn(char, aStr[midIndex+1:])
    
print(isIn("f", "abdflmnopqrst"))


print('Video: Files')
#Great video for learngin about how to use files and modules
'''
open a file named kids with write capability,
ask for a name 2 times, and then write it to the file with each on its
own line
'''

nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter a name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

'''
open a file named kids with read capability,
print out each line in the file
'''
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()


print('Optional Grader')

# find the perimeter of a polygon rounded to 4 decimal places
'''
A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon
'''
import math
def polysum(n, s):
    return round((0.25*n*s**2/math.tan(math.pi/n) + (n*s)**2),4)


s = '1.23,2.4,3.123'

ss = s.split(',')
s1 = ss[0]
s2 = ss[1]
s3 = ss[2]
total = float(s1) + float(s2) + float(s3)
print(total)

    
    
