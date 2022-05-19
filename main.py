import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen()


def move_forwards():
    t.forward(2)


def move_backwards():
    t.backward(2)


def move_counter_clock():
    t.left(2)


def move_clock():
    t.right(2)


def clear_screen():
    t.reset()


def up_right():
    t.circle(-50, 10)
    time.sleep(0.5)

def up_left():
    t.circle(50,10)
    time.sleep(0.5)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_counter_clock)
screen.onkeypress(key="d", fun=move_clock)
screen.onkeypress(key="e", fun=up_right)
screen.onkeypress(key="q", fun=up_left)


screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()