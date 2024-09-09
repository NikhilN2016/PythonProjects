# Import modules
import turtle as trtl
import math 
# Initialize turtle and list of shapes/colors
painter = trtl.Turtle()
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "orange", "blue", "green"]
# Custom functions for creating shapes
def square(side, color):
    if color == 1:
        for x in turtle_colors:
            painter.color(x)
            painter.forward(side)
            painter.right(90)
    elif color == 0:
        painter.color("Black")
        for x in range(4):
            painter.forward(side)
            painter.right(90)
    else:
        print("ERROR: Color parameter can only be 1 (yes) or 0 (no)")
        exit()
# Create base of house
painter.penup()
painter.goto(-50, 0)
painter.pendown()
painter.pensize(5)
square(200, 1)
painter.setheading(90)

# Create roof (45-45-90 triangle)
painter.pensize(2)
legLength = 200/math.sqrt(2)
hyp = legLength * math.sqrt(2)
painter.color("Black")
painter.setheading(45)
painter.forward(legLength)
painter.setheading(-45)
painter.forward(legLength)
painter.setheading(180)
painter.forward(hyp)


# Decorate line between square and triangle with shapes
painter.setheading(0)
for shape in turtle_shapes:
    painter.shape(shape)
    painter.forward(200/len(turtle_shapes))
    if shape != "classic":
        painter.stamp()
# Go to top of triangle
painter.setheading(180)
painter.forward(200/2)
painter.setheading(90)
painter.forward(100)

# Create vertical shapes
painter.pensize(1)
for shape, color in zip(turtle_shapes, turtle_colors):
    painter.shape(shape)
    painter.fillcolor(color)
    painter.forward(30)
    painter.stamp()
painter.shape("arrow")
# Create hexagon on top
painter.circle(40, 360, 6)

painter.penup()
painter.goto(-370, -350)
painter.pendown()
painter.pensize(15)
painter.speed(40)
painter.pencolor("green")
# Create grass
while painter.xcor() < 370:
    painter.setheading(90)
    painter.forward(80)
    painter.setheading(0)
    painter.forward(14)
    painter.setheading(270)
    painter.forward(80)
    painter.setheading(0)
    painter.forward(14)
# Create and maintain turtle screen
wn = trtl.Screen()
wn.mainloop()
