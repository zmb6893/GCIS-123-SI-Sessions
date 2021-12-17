"""
Build a habitat scene for your turtles
@author: Zoe Bingham
"""

import turtle as t
from turtle_utils import reset_turtle, init_scene, draw_arc

# Default values
GRASS_COLOR = "forest green"
CLOUD_COLOR = "white"
ROCK_COLOR = "grey"
SKY_COLOR = "deep sky blue"
ROCK_COLOR = "grey"
PEN_SIZE = 2
GRASS_Y_LEVEL = 0

# Default Screen Values
SCREEN_SIZE = 1080
X_LEFT_EDGE = -540
X_RIGHT_EDGE = 540
Y_BOTTOM_EDGE = -540
Y_TOP_EDGE = 540

def add_grass():
    '''
    This function adds grass to the bottom of your scene (GRASS_Y_LEVEL).
    '''
    
    # Set up drawing
    reset_turtle()
    t.fillcolor(GRASS_COLOR)
    t.pencolor(GRASS_COLOR)

    # Go to the edge of the screen on GRASS_Y_LEVEL and box in grass
    t.goto(X_LEFT_EDGE, GRASS_Y_LEVEL)
    t.pendown()
    t.begin_fill()
    t.goto(X_RIGHT_EDGE, GRASS_Y_LEVEL)
    t.goto(X_RIGHT_EDGE, Y_BOTTOM_EDGE)
    t.goto(X_LEFT_EDGE, Y_BOTTOM_EDGE)
    t.goto(X_LEFT_EDGE, GRASS_Y_LEVEL)
    t.end_fill()

    return

def add_sky():
    '''
    Color the sky
    '''

    # Set up drawing
    reset_turtle()
    t.fillcolor(SKY_COLOR)
    t.pencolor(SKY_COLOR)

    # Box in the sky and fill with blue
    t.goto(X_LEFT_EDGE, GRASS_Y_LEVEL)
    t.pendown()
    t.begin_fill()
    t.goto(X_LEFT_EDGE, Y_TOP_EDGE)


    # Go to the edge of the screen on GRASS_Y_LEVEL and box in grass
    t.goto(X_LEFT_EDGE, GRASS_Y_LEVEL)
    t.pendown()
    t.begin_fill()
    t.goto(X_LEFT_EDGE, Y_TOP_EDGE)
    t.goto(X_RIGHT_EDGE, Y_TOP_EDGE)
    t.goto(X_RIGHT_EDGE, GRASS_Y_LEVEL)
    t.goto(X_LEFT_EDGE, GRASS_Y_LEVEL)
    t.end_fill()

def add_cloud (x_cor, y_cor, size = 1):
    '''
    This function allows you to add clouds of a specified size at a specified location to your scene.

    Parameters:
        :param int size: Size of the cloud
        :param int x_cor: the x coordinate
        :param y_cor: the y coordinate
    '''
    
    # Set up turtle
    reset_turtle()
    t.fillcolor(CLOUD_COLOR)
    t.pencolor(CLOUD_COLOR)

    # Go to the x_cor y_cor location
    t.goto(x_cor, y_cor)
    t.left(180)

    # Draw semi circles to make a cloud
    t.pendown()
    t.begin_fill()
    for curve in range(3):
        draw_arc(180)
        t.left(90)  
    t.end_fill()
    t.goto(x_cor,y_cor)

    # Reset orientation
    t.left(90)

    return

def add_rock(size, color, x_cor, y_cor):
    '''
    This function allows you to add rocks of a specified size and color at a specified location to your scene.

    Parameters:
        :param int size: size of the rock
        :param string color: the color of the rock
    '''

    # Set the rock fill_color to color

    # Go to the x_cor y_cor location

    # Draw an oval

    return

def main():
    init_scene(SCREEN_SIZE)
    add_sky()
    add_grass()
    add_cloud(1,10)
    add_cloud(-400, 100)
    add_cloud(400, 130)
    input("Press enter to exit")

main()