"""
Simple plotting module that will plot data using turtle.

Example:
import plotter

plotter.init("My Graph", "X-Axis", "Y-Axis")
plotter.add_data_point(100)
plotter.add_data_point(25)
plotter.add_data_point(37)
plotter.new_series()
plotter.add_data_point(75)
plotter.add_data_point(65)
plotter.add_data_point(100)
plotter.plot()

@author GCCIS Faculty
"""

import turtle

# constants
__X_LENGTH = 500 # length of x-axis
__Y_LENGTH = 500 # length = y-axis
__MARGIN = 40    # margin size
__COLORS = ["red", "yellow", "blue", "green", "brown", "gold", "orange", 
    "maroon", "violet", "magenta", "purple", "navy", "skyblue", "cyan", 
    "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "black",
    "gray"]

__TITLE = ""          # graph title
__X_AXIS_LABEL = ""   # x axis label
__Y_AXIS_LABEL = ""   # y axis label
__DATA_POINTS = [[]]    # y data points


def reset():
    """
    Resets the plot title, axis labels, and data points.
    """
    __TITLE = ""
    __X_AXIS_LABEL = ""
    __Y_AXIS_LABEL = ""
    __DATA_POINTS.clear()
    new_series()
    turtle.reset()

def title(title=None):
    """
    If the title parameter is not None, it is used to set the plot title.
    Otherwise, returns the current plot title.
    """
    if title is not None:
        global __TITLE
        __TITLE = title
    else:
        return __TITLE

def x_axis_label(label=None):
    """
    If the label parameter is not None, it is used to set the x axis label.
    Otherwise, returns the current x axis label.
    """
    if label is not None:
        global __X_AXIS_LABEL
        __X_AXIS_LABEL = label
    else:
        return __X_AXIS_LABEL

def y_axis_label(label=None):
    """
    If the label parameter is not None, it is used to set the y axis label.
    Otherwise, returns the current y axis label.
    """
    if label is not None:
        global __Y_AXIS_LABEL
        __Y_AXIS_LABEL = label
    else:
        return __Y_AXIS_LABEL

def init(plot_title, x_label, y_label):
    """
    Convenience method that will reset, set the title, x axis label, and y 
    axis label. Any parameter that is None will be ignored.
    """
    reset()
    title(plot_title)
    x_axis_label(x_label)
    y_axis_label(y_label)

def new_series():
    __DATA_POINTS.append([])

def add_data_point(y):
    """
    Adds the specified data point to the plot.
    """
    global __DATA_POINTS
    current = len(__DATA_POINTS) - 1
    __DATA_POINTS[current].append(y)

def __draw_axis(length, ticks, label, right=True):
    """
    Draws an axis and ticks.
    """
    pensize = turtle.pensize()
    
    # draw the label
    turtle.forward(length/2)
    degrees = 90
    if not right:
        degrees = -90
    turtle.right(degrees)
    turtle.forward(20)
    turtle.write(label, align="center")
    turtle.back(20)
    turtle.right(-degrees)
    turtle.back(length/2)

    # draw the axis and ticks
    tick_distance = length / (ticks + 1)
    turtle.pencolor("black")
    turtle.down()

    for i in range(ticks):
        turtle.pensize(3)
        turtle.forward(tick_distance)
        turtle.pensize(1)
        turtle.left(90)
        turtle.forward(5)
        turtle.back(10)
        turtle.forward(5)
        turtle.right(90)
    
    turtle.pensize(3)
    turtle.forward(tick_distance)
    turtle.up()
    turtle.back(length)
    turtle.pensize(pensize)

def plot(trace_plot=True):
    """
    Draws the plot using the turtle.
    """

    # reset the turtle for a new drawing
    turtle.reset()
    turtle.setworldcoordinates(-__MARGIN, -__MARGIN, __X_LENGTH + __MARGIN, 
        __Y_LENGTH + __MARGIN)
    turtle.up()
    
    turtle.tracer(False)
    turtle.setpos(__X_LENGTH/2, __Y_LENGTH + 20)
    turtle.write(__TITLE, align="center")
    turtle.home()

    # draw axes
    number_of_points = len(__DATA_POINTS[0])
    __draw_axis(__X_LENGTH, number_of_points, __X_AXIS_LABEL)
    turtle.left(90)
    __draw_axis(__Y_LENGTH, 10, __Y_AXIS_LABEL, False)

    for i in range(len(__DATA_POINTS)):
        dot_color = __COLORS[i % len(__COLORS)]
        data_points = __DATA_POINTS[i]
        plot_data_points(data_points, dot_color, trace_plot)
    
    turtle.tracer(True)

def plot_data_points(data_points, dot_color, trace_plot=True):
    """
    Plots the current set of data points.
    """
    turtle.tracer(trace_plot)
    # plot data points
    number_of_points = len(data_points)
    x_distance = __X_LENGTH / (number_of_points + 1)
    x = x_distance

    for i in range(number_of_points):
        plot_point(x, data_points[i], dot_color)
        x += x_distance
        turtle.down()
    turtle.up()

def plot_point(x, data_point, dot_color):
    """
    Plots an individual point. If the turtle is down, a line will be drawn to
    the point.
    """
    pensize = turtle.pensize()
    pencolor = turtle.pencolor()
    down = turtle.isdown()

    y = data_point / 100 * __Y_LENGTH

    turtle.setpos(x, y)
    turtle.write(str(data_point))
    turtle.down()
    turtle.pensize(3)
    turtle.pencolor(dot_color)
    turtle.dot()

    # restore the turtle
    turtle.pensize(pensize)
    turtle.pencolor(pencolor)
    if not down:
        turtle.up()
