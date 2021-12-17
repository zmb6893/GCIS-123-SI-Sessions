"""
Week 3: The goal of this activity is to go over functions, turtles, and incremental developement. We will apply these concepts in order to 
create a suprised pikachu.
@author: GCIS-123-16 SI group
"""

# Initialize static global variables for the colors of pikachu
BODY_COLOR = "goldenrod1"
EYE_COLOR = "saddle brown"
NOSE_COLOR = "saddle brown"
CHEEK_COLOR = "firebrick1"
CHEEK_PEN_COLOR = "firebrick4"
DEFAULT_PEN_COLOR = "black"
MOUTH_COLOR = "indianred"
EAR_TIP_COLOR = "saddle brown"

# Import the turtle library and turtle_utils
import turtle as t
import turtle_utils as tu
from habitat_builder import build_default_scene

# Make a function to draw the base of a pikachu (hint: use draw_arc from turtle_utils)
def draw_base(x, y, size):
    '''
    Draw the outline of pikachu and fill it with BODYCOLOR
    '''

    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(DEFAULT_PEN_COLOR)
    t.fillcolor(BODY_COLOR)
    t.tracer(True)

    # Draw the base
    t.begin_fill()
    t.goto(x,y)
    t.forward(100*size)
    t.circle(100 * size)
    t.end_fill()
    t.left(90)
    t.forward(size * 100 + (size * 100 * .25))
    t.left(90)
    t.begin_fill()
    t.circle((size*100) + (size*100) * .25)    
    t.end_fill()
    tu.reset_turtle()

def draw_ear(x, y, direction, size):
    '''
    Draw an ear 
    '''
    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(BODY_COLOR)
    t.fillcolor(BODY_COLOR)

    t.goto((x+(size*50)),(y+(size*100)))
    t.left(direction)
    t.pendown()
    t.begin_fill()
    tu.draw_arc(180, size * .4)
    t.forward(size*200)
    t.end_fill()

    t.left(360-direction)

# Make a function to draw the pikachu eyes
def draw_eye(x,y,size):
    '''
    Draw an eye for pikachu
    '''

    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(DEFAULT_PEN_COLOR)
    t.fillcolor(EYE_COLOR)

    # Draw base eye color
    t.goto(x+(70*size),y+(140*size))
    t.pendown()
    t.begin_fill()
    t.circle(10*size)
    t.end_fill()
    t.penup()

    # Draw shimmer
    t.fillcolor("white")
    t.goto(x+(68*size),y+(140*size))
    t.pendown()
    t.begin_fill()
    t.circle(6*size)
    t.end_fill()
    t.penup()

    tu.reset_turtle()

# Make a function to draw the pikachu nose
def draw_nose(x,y,size):
    ''' 
    Draw a nose for pikachu
    '''

    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(DEFAULT_PEN_COLOR)
    t.fillcolor(NOSE_COLOR)

    # Draw nose
    t.goto(x+(95*size),y+(120*size))
    t.pendown()
    t.begin_fill()
    t.circle(size*5)
    t.penup()
    t.end_fill()

    tu.reset_turtle()

# Make a function to draw the pikachu cheek blush
def draw_cheek(x,y,size):
    '''
    Draw the cheek blush for pikachu
    '''
    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(CHEEK_PEN_COLOR)
    t.fillcolor(CHEEK_COLOR)

    # Draw Blush
    t.goto(x+(50*size),y+(120*size))
    t.pendown()
    t.begin_fill()
    t.circle(20*size)
    t.end_fill()
    t.penup()

    tu.reset_turtle()


# Make a function to draw the pikachu mouth
def draw_mouth(x,y,size):
    ''' 
    Draw the suprised pikachu mouth
    '''

    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    # Set fill and pen colors
    t.pencolor(DEFAULT_PEN_COLOR)
    t.fillcolor(MOUTH_COLOR)

    # Draw mouth
    t.goto(x+(95*size),y+(100*size))
    t.pendown()
    t.begin_fill()
    t.circle(20*size)
    t.end_fill()
    t.penup()

    tu.reset_turtle()

# Make a function that puts all of the elements of pikachu together with parameters for the x and y coords and size
def draw_pikachu(x, y, size):
    ''' 
    Draw suprised pikachu
    '''

    # Set pen to up and add max drawing speed
    tu.reset_turtle()

    draw_base(x, y, size)
    draw_ear(x, y, 110, size)
    draw_ear(x+(100*size), y, 220, size)
    draw_eye(x,y,size)
    draw_eye(x+(50*size),y,size)
    draw_nose(x,y, size)
    draw_cheek(x,y,size)
    draw_cheek(x+(100*size),y,size)
    draw_mouth(x,y,size)
    t.right(180)

    tu.reset_turtle()

# Call our pikachu function multiple times
def main():
    tu.init_scene()
    build_default_scene()

    draw_pikachu(-500, -50, .5)
    draw_pikachu(0, 0, 1)
    draw_pikachu(300, -10, 1.5)

    input("Press Enter to Continue")

main()