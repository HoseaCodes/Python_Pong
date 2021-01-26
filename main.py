from turtle import Screen
from new_player import Player
from score_board import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # delay update

player_one = Player((350, 0))
player_two = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")

screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y

    if ball.distance(player_one) < 50 and ball.xcor() > 320 or ball.distance(player_two) < 50 and ball.xcor() > -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()