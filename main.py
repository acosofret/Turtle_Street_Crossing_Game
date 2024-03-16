from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from road import Road
from display_messages import GameOver
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.colormode(255)

player = Player()
car_manager = CarManager()
road = Road()
road.draw_limits()
screen.onkey(player.move, "Up")
frame_no = 0
car_step_break = 0.3
game_over = GameOver

# Create a scoreboard that keeps track of which level the user is on
scoreboard = Scoreboard()

game_in_on = True
while game_in_on:
    time.sleep(car_step_break)
    screen.update()
    frame_no += 1
    if frame_no % 6 == 0:
        car_manager.create_new_car()
    car_manager.move_cars()

# Detect when the turtle player collides with a car and stop the game
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_in_on = False
            game_over.game_over_message(self=GameOver())



# Detect when the turtle player has reached the top edge of the screen, return the turtle to the start
# and increase the speed of the cars
    if player.ycor() > 250:
        player.start_new_level()
        scoreboard.update_level()
        car_step_break *= 0.9




screen.exitonclick()
