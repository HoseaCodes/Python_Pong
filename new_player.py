from turtle import Turtle

STARTING_POSITION = [(-270, 0), (-270, 20), (-270, 40),  (-270, 60)]


class Player(Turtle):

    def __init__(self):
        super().__init__
        self.create_player()

    def create_player(self):
        for position in STARTING_POSITION:
            player = Turtle(shape="square")
            player.penup()
            player.color("white")
            player.goto(position)