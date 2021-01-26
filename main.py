from turtle import Screen
from new_player import Player
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
#screen.tracer(0) # delay update

player_one = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")


game_is_on = True
while game_is_on:
    player_one.move()



screen.exitonclick()