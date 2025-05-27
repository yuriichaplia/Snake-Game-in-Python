from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]

class Snake:
    def __init__(self):
        self.segments = []
        position_x = 0

        for _ in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x=position_x, y=0)
            position_x -= 20
            self.segments.append(segment)

        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        position_x = 0
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(x=position_x, y=0)
            position_x -= 20
            self.segments.append(segment)

        self.head = self.segments[0]

    def extend(self):
        position = self.segments[len(self.segments)-1].position()
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[new_segment - 1].xcor()
            new_y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS[3]:
            self.head.setheading(DIRECTIONS[1])

    def down(self):
        if self.head.heading() != DIRECTIONS[1]:
            self.head.setheading(DIRECTIONS[3])

    def right(self):
        if self.head.heading() != DIRECTIONS[2]:
            self.head.setheading(DIRECTIONS[0])

    def left(self):
        if self.head.heading() != DIRECTIONS[0]:
            self.head.setheading(DIRECTIONS[2])


