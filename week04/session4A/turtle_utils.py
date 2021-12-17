"""
Shortcut functions for turtle
@author: Zoe Bingham
"""

import turtle as t

# Default values
SCREEN_SIZE = 1080

def reset_turtle():
    '''
    Resets the turtle to prepare for new drawing
    '''
    t.tracer(False)
    t.penup()
    t.goto(0,0)
    t.speed(0)
    t.pencolor("black")

def init_scene(size = SCREEN_SIZE):
    '''
    Initializes the screen size of the scene to be size by size
    Parameters:
    :param int size: The x and y dimensions of the turtle screen
    '''
    t.screensize(size, size)

def draw_arc(degrees, size = 1):
    '''
    Draws an arc with a length of degrees
    Parameters:
    :param int degrees: The size and curve of the arc
    '''
    for increment in range(degrees):
        t.forward(size)
        t.right(1)