#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:01:06 2017

@author: davidbass
"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x / y is", x/y)
        
elif x < y:
    print ("x is smaller")
else:
    print("y is smaller")
print("thanks!")