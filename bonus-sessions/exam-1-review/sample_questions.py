"""
Practicum 1 Review: Functions, Turtle, Testing, Loops, Conditionals
@author: Zoe Bingham
""" 

# Let's start with making a new github branch! How would we do that?

# Use TDD for these functions

def radians_to_degrees(radians):
    '''
    Make a function that translates radians to degrees, given radians. Use this equation: radian * (180/pi) = degrees.

    Parameters:
    :param float radians: radians to be converted to degrees

    :return float degrees: the number of degrees equivalent to radians
    '''
    pass

def did_i_pass():
    '''
    Make a function that takes in input for the score and returns true if the score is more than or equal to 70 and false if under 70.

    :return boolean: whether or not you passed
    '''
    pass

def calculate_grade(score):
    '''
    Calculate the grade a student has and return the grade as A-90-100, B-80-90, C-70-80, D60-70, or O_O-less than 60

    Parameters:
    :param float score: the score of the examee (ex: 93.2)

    :return string: return the grade letter of the score
    '''
    pass

def make_emoji_with_input():
    '''
    Make a function that returns emojis for the input string. (EX: '0 O p P Q' becomes '0_-\n'O_-\np_-\nQ_q\n')   

    :return string: returns a string of emojis separated by a new line 
    '''
    pass

# Incremental Stuff Below

def draw_closed_semi(x,y,size):
    '''
    Make a function that draws a semi circle closed at the bottom at x y with a default size of 100

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    '''
    pass

def draw_shell(x,y,size,color):
    '''
    Make a function that draws a shell at x, y, of size and shell_color. default color should be green

    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the shell
    '''
    pass

def draw_eye(x,y,size,color):
    '''
    Make a function that draws an eye at x, y with a size and color

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the pupil
    '''
    pass

def draw_head(x,y,size,color):
    '''
    Make a function that draws the head of the turtle. default head color should be green
    
    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the head
    '''
    pass

def draw_legs(x,y,size,color):
    '''
    Make a function that draws all four legs of the turtle.

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string color: color of the legs
    '''
    pass

def draw_turtle(x,y,size,shell_color,eye_color):
    '''
    Make a function that draws a turtle. View the board.

    Parameters:
    :param int x: x location
    :param int y: y location
    :param float size: scalar to determine size
    :param string shell_color: color of the turtle shell
    :param string eye_color: color of the eye
    '''
    pass