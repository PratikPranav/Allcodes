# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:20:17 2022

@author: Pratik
"""

def rps(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    
    if(pl1[p1]==pl2[p2]):
        print("draw")
    else:
       if(pl1[p1]=="rock" and pl2[p2]=="sciscor"):
            print("player 1 wins")
       elif(pl1[p1]=="rock" and pl2[p2]=="paper"):
          print("playr two wins")
        
    
    
    
    
pl1={0:'rock',1:"paper",2:"scisor"}
pl2={0:'paper',1:"rock",2:"scisor"}
    
while(1):
    num1=input("p1 enter your choice")
    num2=input("p2 enter your choice")
    bit1=int(input("p1 enter your secret bit position"))
    bit2=int(input("p2 enter your secret bit position"))
        
    rps(num1,num2,bit1,bit2)
    c=input("do you want to continue? y/n")
    if c=='n':
       break