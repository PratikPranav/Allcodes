# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:14:18 2022

@author: Pratik
"""

n=input("enter your name")
a=int(input('enter your age '))
print("Your name is ",n," and your age is ",a)

p=float(input("enter the price of your phone which you want to sell"))

if (a<21):
   print("O wow! since you are below 21 \n youll get a special offer of 20%")
   d=0.2*p
   print("so you'l get",p,"+",d," i.e ",p+d) 
else:
   print("ok so u r getting",p+100)