# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:56:36 2022

@author: Pratik
"""

import turtle
#turtle.bgcolor("black")
tur = turtle.Turtle()  #tur is pen
tur.speed(1)
width=5
height=7

tur.setpos(-150,150)

for i in range(5):
    tur.forward(50)
    tur.right(80)
    tur.left(10)
    tur.back(5)
    tur.dot()
    
turtle.done()