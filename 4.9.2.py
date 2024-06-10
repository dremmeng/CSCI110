from turtle import *


def draw_square(size):
    penup()
    goto(0, 0)
    setheading(90)
    backward(size//2)
    setheading(0)
    backward(size//2)
    pendown()
    pencolor("pink")
    for i in [1,2,3,4]:
        forward(size)
        left(90)
for size in [20,40,60,80]:
    draw_square(size)