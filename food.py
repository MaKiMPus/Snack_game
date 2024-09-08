from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        randomlocation_x = random.randint(-325,325)
        randomlocation_y = random.randint(-325, 325)
        self.goto(randomlocation_x, randomlocation_y)
        self.refresh_location()

    def refresh_location(self):
        randomlocation_x = random.randint(-325, 325)
        randomlocation_y = random.randint(-325, 325)
        self.goto(randomlocation_x, randomlocation_y)
