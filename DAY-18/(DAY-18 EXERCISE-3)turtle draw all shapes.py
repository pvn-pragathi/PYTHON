from turtle import Turtle, Screen
import random

turtle = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.right(angle)
        turtle.forward(100)


for shape_side_n in range(3,11):
    turtle.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()