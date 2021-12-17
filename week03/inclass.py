import turtle as t

"""
INCLASS SOLUTION: Draw a smiley face.
"""

def draw_centered_circle(x, y, radius, size):
    # Draw a circle with a center at (x,y)
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.circle(radius * size)
    t.penup()

def draw_smile(x, y, radius, size):
    # Draw an arc and line
    t.goto(x - ((radius * size) / 3), y - ((radius * size) / 3))
    t.pendown()
    t.setheading(270)
    t.circle(radius*size/3, 180)
    t.left(90)
    t.forward(2*radius*size/3)
    t.penup()

def draw_eye(x, y, radius, size):
    t.goto(x,y)
    t.pendown()
    t.circle(radius*size/6)
    t.penup()


def draw_smiley(x,y,radius,size):
    t.tracer(False)
    draw_centered_circle(x, y, radius, size)
    draw_smile(x, y, radius, size)
    draw_eye(x + radius/3,y + radius/3,radius,size)
    draw_eye(x - radius/3 ,y + radius/3,radius,size)
    t.setheading(0)

draw_smiley('0', 0, 100, 1)
draw_smiley(50, 50, 100, .5)
input("Enter")