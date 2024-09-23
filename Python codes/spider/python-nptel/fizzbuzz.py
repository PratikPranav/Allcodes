# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:05:48 2022

@author: Pratik
"""

for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(i,"=fizzbuzz")
    else:
        if(i%3==0):
           print(str(i)+"=fizz")
        else:
            if(i%5==0):
                print(str(i)+"=buzz")
            else:
                print(str(i))#print(i)
                