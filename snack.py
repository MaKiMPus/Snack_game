from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snack:

    def __init__(self):
        self.segments = []
        self.createsnack()
        self.head = self.segments[0]

    def createsnack(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snack = Turtle(shape="square")
        snack.color("white")
        snack.penup()
        snack.goto(position)
        self.segments.append(snack)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for num_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_seg - 1].xcor()
            new_y = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





