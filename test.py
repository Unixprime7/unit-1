import turtle
from turtle import *
t = Turtle()
t.speed(100)


def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)


def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length + 5
        t.left(5)
addSquares(100)

turtle.done()