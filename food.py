from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("Red")
        self.replace_food()
        self.showturtle()

    def replace_food(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.setpos(x, y)
