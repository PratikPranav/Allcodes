# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:57:01 2022

@author: Pratik
"""
def ls(n,x):
   ele=[]
   for i in range(1,n):
      ele.append(i)
      c=0
      f=0
      for i in ele:
          if i==x:
              print(x," is found at ",i)
              f=1
              break
          if f==0:
              print(x,"not found")
              print("no of iteration :",str(c))
              break
ls(5,2)