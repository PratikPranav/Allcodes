# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:25:57 2022

@author: Pratik
"""

currency={}

currency["dollar"]=60
print(currency)

currency.items()  #print all items in dictionary named currency
print(currency)

currency["dollar"]=74     #updates the dictionary currency
print(currency)

currency["rupee"]=1    #inserts
currency['yen']=60
print(currency)

del currency["yen"]
print(currency)

rupee = 10
r=10
rs=r*currency['rupee']
print(rs)