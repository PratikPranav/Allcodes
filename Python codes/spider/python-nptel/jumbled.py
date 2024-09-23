# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:48:06 2022

@author: Pratik
"""
import random
def choose():
    words=['basket',"computer",'rainbow',"buffalo"]
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
def play():
    p1name=input("enter your name")
    p2name=input("enter your name")
    pp1=0
    pp2=0
    turn=0

    while(1):
          pword=choose()
          q=jumble(pword)
          print(q)
     
          if(turn%2==0):
             print(p1name,"your turn")
             ans=input("enter the correct word")
             if(ans==pword):
                pp1+=1
                print("Great u r correct , your score is :",pp1)
             else:
                print("oops u r wrong , it was :",pword)
                print("And your score is :",pp1)
                c=int(input("do u want to play again ? 1 or 0"))
              
                if c==0:
                  print("Thanks for playing both of you ")
                  print(p1name," score is:",pp1 ," and ",p2name ,"score is",pp2)
                  break
          else:
              print(p2name,"your turn")
              ans=input("enter the correct word")
              if(ans==pword):
                 pp2+=1
                 print("Great u r correct , your score is :",pp2)
              else:
                 print("oops u r wrong , it was :",pword)
                 print("And your score is :",pp2)
                 c=int(input("do u want to play again ? 1 or 0"))
               
                 if c==0:
                   print("Thanks for playing both of you ")
                   print(p1name," score is:",pp1 ," and ",p2name ,"score is",pp2)
                   break
          turn = turn + 1
          
play()
                  