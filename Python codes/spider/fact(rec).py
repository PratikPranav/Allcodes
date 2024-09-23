# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:04:25 2022

@author: Pratik
"""

def fact(n):
    if n==1:
        return 1
    elif n<1:
        return 0
    else:
        return n*fact(n-1)


print(fact(3))