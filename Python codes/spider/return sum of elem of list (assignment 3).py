# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 17:21:02 2022

@author: Pratik
"""

def sum_of_list(L):
    
    total = 0
    
    for i  in range(len(L)):
        total = total + L[i]
        
    return total 
    
L = [1,2,3,4,5,6,7,8,9,10]
total_sum = sum_of_list(L)
print(total_sum)