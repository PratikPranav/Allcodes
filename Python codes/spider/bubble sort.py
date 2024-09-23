# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:27:56 2022

@author: Pratik
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
               temp=a[j]
               a[j]=a[j+1]
               a[j+1]=temp
               
a=[5,2,6,4,3]
bubble(a)
for i in a:
    print(i)