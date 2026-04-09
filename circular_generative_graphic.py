import turtle
import math
import random
from colorspace import sequential_hcl

t = turtle.Turtle()
t.speed(0)
t.pensize(6)

screen = turtle.Screen()
screen.bgcolor("navy")
screen.tracer(0, 0)

turtle.colormode(255)

# Create a continuous range of colors (256 shades) between two colors
palette = sequential_hcl(h=[260, 10], c=80, l=[30, 90], n=256)
color_range = [tuple(int(x * 255) for x in color[:3]) for color in palette.colors()]

def random_color():
    """Get a random color from the continuous gradient"""
    return random.choice(color_range)

def draw_shape():
    t.penup()
    t.goto(-200, math.sin(-200 / 20) * 50)
    t.pendown()
    for x in range(-200, 200):
        y = math.sin(x / 20) * 50  # Adjust 20 for frequency, 50 for height
        t.pencolor(random_color())
        t.goto(x, y)
    screen.update()

draw_shape()
turtle.done()