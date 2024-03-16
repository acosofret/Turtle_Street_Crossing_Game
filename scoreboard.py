from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(0, 290)
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 18, "normal"))

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(0, 290)
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 18, "normal"))