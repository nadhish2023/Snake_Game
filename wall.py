from turtle import Turtle

timmy = Turtle()

def move_front():
    for i in range(12):
        timmy.pendown()
        timmy.forward(40)
        timmy.penup()
        timmy.forward(10)
    timmy.pendown()
    timmy.forward(20)
    timmy.penup()

def make_wall():
    timmy.color("White")
    timmy.hideturtle()
    timmy.penup()
    timmy.width(3)
    timmy.speed("fastest")
    timmy.goto(-310,-310)
    for line in range(4):
        move_front()
        timmy.left(90)

