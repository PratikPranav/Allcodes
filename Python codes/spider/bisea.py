# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:33:05 2022

@author: Pratik
"""

a=[]
n=int(input("enter how many elements you want to insert"))

for i in range(n):
    e=input("enter the elements")
    a.append(i)
    
s=int(input("enter the element you want to search"))
for i in range(a):
   if(s==a[i]):
      print("no found")
   else: 
    print("not found") 