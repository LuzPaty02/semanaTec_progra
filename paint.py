"""Paint, for drawing shapes.

Exercises:
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector

def line(start, end):
    """Draw a line from the starting point to the end point.

    Args:
        start (vector): Starting point of the line.
        end (vector): End point of the line.
    """
    up()  # Lift the pen up
    goto(start.x, start.y)  # Move to the start position
    down()  # Place the pen down
    goto(end.x, end.y)  # Draw line to the end position

def square(start, end):
    """Draw a square from the starting point to the end point.

    Args:
        start (vector): Starting point of the square.
        end (vector): End point used to define square size.
    """
    up()
    goto(start.x, start.y)  # Move to the start position
    down()
    begin_fill()

    for count in range(4):  # Draw four sides of the square
        forward(end.x - start.x)
        left(90)

    end_fill()

# Added the function to draw a circle
def draw_circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    goto(start.x, start.y - radius)
    circle(radius)

    end_fill()

# Added the function to draw a rectangle
def rectangle(start, end):
    """Draw a rectangle from the start to the end point.

    Args:
        start (vector): Starting point of the rectangle.
        end (vector): Defines the opposite corner of the rectangle.
    """
    up()
    goto(start.x, start.y) 
    down()
    begin_fill()

    width = end.x - start.x  # Calculate the width
    height = end.y - start.y  # Calculate the height

    for _ in range(2):  # Draw the rectangle using two width and two height segments
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


# Added the function to draw a triangle
def triangle(start, end):
    """Draw an equilateral triangle from the start to the end point.

    Args:
        start (vector): Starting point of the triangle.
        end (vector): Defines the size of the triangle.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):  # Draw three sides of the triangle
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    """Handle screen taps to store the starting point or draw a shape.

    Args:
        x (float): X-coordinate of the tap.
        y (float): Y-coordinate of the tap.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)  # Store starting point
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)  # Draw the selected shape
        state['start'] = None  # Reset starting point

def store(key, value):
    """Store a value in the global state.

    Args:
        key (str): The key where the value will be stored.
        value: The value to store (e.g., a shape function or color).
    """
    state[key] = value

# Initialize state with no starting point and default shape as line
state = {'start': None, 'shape': line}

# Setup the drawing window
setup(420, 420, 370, 0)

# Bind the mouse click to the 'tap' function
onscreenclick(tap)

# Listen for keyboard events
listen()

# Bind 'u' key to undo the last action
onkey(undo, 'u')

# Bind color keys for changing the drawing color
onkey(lambda: color('yellow'), 'Y')  # Added new color: yellow
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
