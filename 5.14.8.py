import turtle


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        col = "red"
    elif height < 200 and height >= 100:
        col = "yellow"
    elif height < 100:
        col = "green"
    t.begin_fill()           # Added this line
    t.left(90)
    t.color(col)
    t.forward(height)

    
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.color("black")
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()