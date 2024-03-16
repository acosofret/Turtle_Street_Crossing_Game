from turtle import Turtle


class GameOver(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()

	def game_over_message(self):
		self.goto(0, 260)
		self.write(arg="GAME OVER", align="center", font=("Courier", 20, "bold"))
