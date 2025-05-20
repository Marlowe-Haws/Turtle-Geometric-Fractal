import turtle

turtle.colormode(255)

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

def draw_polygons_grouped():
    draw_polygons()
    my_turtle.right(90)
    draw_polygons()
    my_turtle.right(90)
    draw_polygons()
    my_turtle.right(90)
    draw_polygons()

my_screen = turtle.Screen()
my_screen.setup(width=950, height=950)
my_screen.bgcolor(0, 0, 0)
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.goto(25, -25)
my_turtle.shape("turtle")
my_turtle.fillcolor(0, 127, 0)

for _ in range(4):
    draw_polygons_grouped()
    my_turtle.forward(100)

my_screen.exitonclick()
