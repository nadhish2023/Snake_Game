from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for k in range(3):
            new_segment = Turtle("square")
            new_segment.width(10)
            new_segment.color("green")
            new_segment.fillcolor("yellow")
            new_segment.penup()
            new_segment.goto(k*(-20),0)
            self.segments.append(new_segment)
        self.segments[0].color("red")
        self.segments[0].fillcolor("yellow")


    def collide(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if abs(head.xcor() - segment.xcor()) < 1e-9 and abs(head.ycor() - segment.ycor()) < 1e-9:
                return True
        return False

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.color("green")
        new_segment.fillcolor("yellow")
        position=self.segments[-1].pos()
        dir=self.segments[-1].heading()
        if dir==90:
            pos=(position[0],position[1]-20)
        elif dir==0:
            pos = (position[0]-20, position[1])
        elif dir==180:
            pos = (position[0]+20, position[1])
        else:
            pos = (position[0], position[1] + 20)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
