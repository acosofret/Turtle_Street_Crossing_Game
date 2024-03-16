from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_new_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(x=310, y=random.randint(-240, 240))
        self.all_cars.append(new_car)

    def move_cars(self):
        for x in self.all_cars:
            x.forward(MOVE_INCREMENT)




