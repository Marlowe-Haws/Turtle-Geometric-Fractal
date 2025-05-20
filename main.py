# A simple program using the turtle module to make a fractal composed of basic geometric shapes.
import turtle

# I like the RBG color model.
turtle.colormode(255)

# Here are the functions for each of the geometric shapes.
# I made every polygon equilateral with all sides 100 pixels in length.
# I rotated through rainbow colors, with slight alterations on repeated colors.
def draw_triangle():
    my_turtle.pencolor((255, 0, 0))
    for _ in range(3):
        my_turtle.forward(100)
        my_turtle.left(120)

def draw_square():
    my_turtle.pencolor(255, 165, 0)
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)

def draw_pentagon():
    my_turtle.pencolor(255, 255, 0)
    for _ in range(5):
        my_turtle.forward(100)
        my_turtle.left(72)

def draw_hexagon():
    my_turtle.pencolor(0, 255, 0)
    for _ in range(6):
        my_turtle.forward(100)
        my_turtle.left(60)

def draw_heptagon():
    my_turtle.pencolor(0, 0, 255)
    for _ in range(7):
        my_turtle.forward(100)
        my_turtle.left(51.43)

def draw_octagon():
    my_turtle.pencolor(65, 0, 255)
    for _ in range(8):
        my_turtle.forward(100)
        my_turtle.left(45)

def draw_nonagon():
    my_turtle.pencolor(127, 0, 255)
    for _ in range(9):
        my_turtle.forward(100)
        my_turtle.left(40)

def draw_decagon():
    my_turtle.pencolor(255, 0, 65)
    for _ in range(10):
        my_turtle.forward(100)
        my_turtle.left(36)

def draw_hendecagon():
    my_turtle.pencolor(255, 165, 65)
    for _ in range(11):
        my_turtle.forward(100)
        my_turtle.left(32.73)

def draw_dodecagon():
    my_turtle.pencolor(255, 255, 65)
    for _ in range(12):
        my_turtle.forward(100)
        my_turtle.left(30)

# I made a function to draw all the shapes with a common starting point.
# I decided to draw the shapes in descending order of number of sides.
# Since lines are drawn over prior lines, I wanted the smaller shapes to be drawn last to stand out more.
def draw_polygons():
    draw_dodecagon()
    draw_hendecagon()
    draw_decagon()
    draw_nonagon()
    draw_octagon()
    draw_heptagon()
    draw_hexagon()
    draw_pentagon()
    draw_square()
    draw_triangle()

# This function alternates between calling the previous function and rotating right.
# It draws 4 groups of 12 shapes, then finishes facing 90 degrees to the left of its original orientation.
def draw_polygons_grouped():
    draw_polygons()
    for _ in range(3):
        my_turtle.right(90)
        draw_polygons()

# Here we initialize the screen and turtle objects.
# The fractal involves moving up and to the left, so I adjusted the starting location to be down and to the right a little to center the image better.
# The iterative nature of the fractal takes a while, so I set max speed.
# I chose a black background and dark green turtle.
my_screen = turtle.Screen()
my_screen.setup(width=950, height=950)
my_screen.bgcolor(0, 0, 0)
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.goto(25, -25)
my_turtle.shape("turtle")
my_turtle.fillcolor(0, 127, 0)

# Because of the rotation involved in the previous function, we can simply call it, move forward, and repeat.
# Repeating 4 times results in a fractal that concludes at its starting point, after traversing a square-shaped path.
for _ in range(4):
    draw_polygons_grouped()
    my_turtle.forward(100)

# You could continue indefinitely doubling the distance moved.
# for _ in range(4):
#     draw_polygons_grouped()
#     my_turtle.forward(200)
#
# You could also double the lengths of the sides of the polygons.
# You could pass an argument to adjust side length.
# def triangle(side_length):
# my_turtle.pencolor((255, 0, 0))
#     for _ in range(3):
#         my_turtle.forward(side_length)
#         my_turtle.left(120)
# Continue passing the argument through the chain of calling functions.
my_screen.exitonclick()
