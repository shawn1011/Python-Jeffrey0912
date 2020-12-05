# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:32:09 2020

@author: user
"""

import turtle
tur = turtle.Turtle()
tur.penup()
turtle.setup(500,500)
tur.goto(-100,100)
tur.pendown()

def square():
        for i in range(6):
            tur.forward(100)
            tur.right(60)
            
tur.fillcolor("#FF0000")



tur.begin_fill()
square()

tur.end_fill()

turtle.done()
turtle.exitonclick()