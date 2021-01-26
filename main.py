from turtle import Screen
from new_player import Player
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # delay update

player_one = Player((350, 0))
player_two = Player((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")

screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")


game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()