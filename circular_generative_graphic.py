import turtle
import math
from colorspace import rainbow_hcl

t = turtle.Turtle()
t.speed(0)
t.pensize(25)


screen = turtle.Screen()
screen.bgcolor("#010140")
screen.tracer(0, 0)
phase = 16

# Create a full-spectrum HCL rainbow palette (256 shades)
palette = rainbow_hcl(c=90, l=40)
color_range = palette.colors(256)

def draw_shape():
    x_start = -200
    x_end = 200
    wavelength = 30
    amplitude = 80
    

    t.penup()
    t.goto(x_start, math.sin((x_start / wavelength) + phase) * amplitude)
    t.pendown()

    for x in range(x_start, x_end + 1):
        y = math.sin((x / wavelength) + phase) * amplitude
        color_index = int((x - x_start) / (x_end - x_start) * (len(color_range) - 1))
        t.pencolor(color_range[color_index])
        t.goto(x, y)

    screen.update()

def animate():
    global phase
    t.clear()
    phase += 0.08
    draw_shape()
    screen.ontimer(animate, 16)

def draw_design():
    draw_shape()

"""screen.listen()
screen.onkey(, "space")
screen.onkey(, "Escape")
screen.onkey(, "q")
screen.onclick()"""

animate()
turtle.done()