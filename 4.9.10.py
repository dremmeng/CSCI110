from turtle import *

def drawstar():
    #Loop five times
    for i in [1, 2, 3, 4, 5]:
        # moving turtle 100 units forward
        forward(100)
        # rotating turtle 144 degree right
        right(144)


#Loop five times
for i in [1,2,3,4,5]:
    penup()
    forward(350)
    right(144)
    pendown()
    drawstar()

