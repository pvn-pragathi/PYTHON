import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
t = turtle_module.Turtle()
t.speed("fastest")
t.hideturtle()
color_list = [(185, 18, 44), (241, 231, 69), (251, 231, 237), (218, 238, 245), (192, 74, 35),(22, 123, 169), (110, 181, 206), (215, 68, 108), (16, 140, 88), (194, 175, 20), (208, 153, 96), (181, 43, 64),(16, 166, 212),(23, 38, 73), (77, 173, 96), (240, 230, 3), (37, 45, 111), (216, 133, 156), (211, 74, 55),(125, 184, 123), (234, 167, 184), (8, 58, 38), (148, 209, 220), (9, 94, 54), (164, 29, 27), (7, 85, 109),(232, 172, 166), (162, 212, 179)]

t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots + 1):
    t.dot(20,random.choice(color_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

