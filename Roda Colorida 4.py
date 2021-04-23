# -*- coding: utf-8 -*-
import turtle as t
t.Screen()
t.speed(0)
t.pensize()

for i in range(125):
    t.right(30)
    for colours in ['violet' , 'indigo' , 'blue' , 'green' , 'yellow' , 'orange' , 'red']:
        t.color(colours)
        t.forward(2*i)
        t.left(20)
        t.forward(2*i)
        t.left(120)
        t.forward(2*i+4)
        t.left(120)
t.exitonclick()
