import turtle
import math
from colorspace import rainbow_hcl

t = turtle.Turtle()
t.speed(0)
t.pensize(50)


screen = turtle.Screen()
screen.bgcolor("#000066")
screen.tracer(0, 0)

# Create a full-spectrum HCL rainbow palette (256 shades)
palette = rainbow_hcl(c=250, l=50)
color_range = palette.colors(256)

def draw_shape():
    x_start = -200
    x_end = 200
    frequency = 40
    amplitude = 50

    t.penup()
    t.goto(x_start, math.sin(x_start / frequency) * amplitude)
    t.pendown()

    for x in range(x_start, x_end + 1):
        y = math.sin(x / frequency) * amplitude
        color_index = int((x - x_start) / (x_end - x_start) * (len(color_range) - 1))
        t.pencolor(color_range[color_index])
        t.goto(x, y)

    screen.update()

draw_shape()
turtle.done()