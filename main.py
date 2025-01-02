from turtle import Screen
from snake import *
from food import *
from high_score import *
import wall
import time

myscreen=Screen()
myscreen.tracer(0)
myscreen.title("Snake Game")
myscreen.setup(width=650, height=650,startx=400, starty=0)
myscreen.bgpic("image1.gif")
myscreen.listen()
wall.make_wall()

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("White")
writer.goto(0, 0)
writer.write("WELCOME", align="center", font=("Arial", 24, "normal"))
myscreen.update()

writer1 = Turtle()
writer1.hideturtle()
writer1.penup()
writer1.color("White")

time.sleep(1)

snake=Snake()
food=Food()

myscreen.onkey(fun=snake.go_up,key="Up")
myscreen.onkey(fun=snake.go_down,key="Down")
myscreen.onkey(fun=snake.go_right,key="Right")
myscreen.onkey(fun=snake.go_left,key="Left")

myscreen.onkey(fun=snake.go_up,key="W")
myscreen.onkey(fun=snake.go_down,key="S")
myscreen.onkey(fun=snake.go_right,key="D")
myscreen.onkey(fun=snake.go_left,key="A")

myscreen.onkey(fun=snake.go_up,key="w")
myscreen.onkey(fun=snake.go_down,key="s")
myscreen.onkey(fun=snake.go_right,key="d")
myscreen.onkey(fun=snake.go_left,key="a")

game_is_on=True
score=0
highscore=read_highscore()
writer1.goto(0,220)
writer1.write(f"HighScore:{highscore}", align="center", font=("Arial", 14, "normal"))

writer.goto(0, 250)
writer.clear()

def update_score():
    global score,highscore
    if score > highscore:
        write_high_score(score)
    highscore=read_highscore()
    writer.clear()
    writer.write(f"Score:{score}", align="center", font=("Arial", 24, "normal"))
    writer1.clear()
    writer1.write(f"HighScore:{highscore}", align="center", font=("Arial", 14, "normal"))

def call_error():
    global game_is_on
    print("GAME OVER")
    game_is_on=False

message="hello"

while game_is_on:
    myscreen.update()
    time.sleep(0.1)
    snake.move()
    if snake.collide():
        message="Collision With Tail"
        call_error()
    if not -300 <= snake.head.xcor() <= 300:
        message = "Collision With wall"
        call_error()
    if not -300 <= snake.head.ycor() <= 300:
        message = "Collision With wall"
        call_error()
    if snake.head.distance(food)<5:
        score+=5
        food.replace_food()
        snake.add_segment()
        print("New Score :",score)
    update_score()

writer.goto(0, 0)
writer.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
writer1=Turtle()
writer1.hideturtle()
writer1.penup()
writer1.color("Red")
writer1.goto(0, -50)
writer1.write(message, align="center", font=("Arial", 30, "normal"))
myscreen.update()


myscreen.exitonclick()