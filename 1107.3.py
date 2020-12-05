# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:20:01 2020

@author: user
"""

import turtle
tur = turtle.Turtle()
turtle.setup(500,500)


def rectangle():
    tur.forward(80)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(80)
    tur.right(90)
    tur.forward(200)
    tur.right(90)

tur.penup()
tur.goto(100,200)
tur.pendown()

tur.fillcolor(0,0,1)
tur.begin_fill()
rectangle()
tur.end_fill()


tur.penup()
tur.goto(180,200)
tur.pendown()

tur.fillcolor(1,1,1)
tur.begin_fill()
rectangle()
tur.end_fill()


tur.penup()
tur.goto(260,200)
tur.pendown()

tur.fillcolor(1,0,0)
tur.begin_fill()
rectangle()
tur.end_fill()


turtle.done()

