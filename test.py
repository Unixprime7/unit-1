import turtle
from turtle import *
t = Turtle()
t.speed(100)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90)

turtle.done()