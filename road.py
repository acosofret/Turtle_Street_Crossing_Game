from turtle import Turtle
import random


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()


    def draw_limits(self):
        self.color("white")
        self.penup()
        self.goto(x=-300, y=-250)
        self.pendown()
        self.goto(x=300, y=-250)
        self.penup()
        self.goto(x=300, y=250)
        self.pendown()
        self.goto(x=-300, y=250)

