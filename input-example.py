#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:26:32 2017

@author: davidbass
"""

x = int(input('Enter an integer: '))
if x%2 == 0:
    print ('')
    print ('x is Even')
elif x%3 == 0:
    print ('x is divided by 3')
else:
    print ('x is odd')