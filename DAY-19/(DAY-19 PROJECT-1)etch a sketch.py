import turtle as turtle_module

t = turtle_module.Turtle()
screen = turtle_module.Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def turn_right():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()


