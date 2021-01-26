from turtle import Turtle

STARTING_POSITION = [(-270, 0), (-270, 20), (-270, 40),  (-270, 60)]
STARTING_POSITION_TWO = [(270, 0), (270, 20), (270, 40),  (270, 60)]
up = 90
down = 270
move_distance = 20

class Player(Turtle):

    def __init__(self):
        super().__init__
        self.player_body = []
        self.create_player()
        self.head = self.player_body[0]

    def create_player(self):
        for position in STARTING_POSITION:
            self.player_shape(position)
        for position in STARTING_POSITION_TWO:
            self.player_shape(position)

    def player_shape(self, position):
        player = Turtle(shape="square")
        player.penup()
        player.color("white")
        player.goto(position)
        self.player_body.append(player)

    def move(self):
        for seg in self.player_body:
            seg.forward(20)
        #for index in range(len(self.player_body) - 1, -1):
         #   new_x = self.player_body[index - 1].xcor()
          #  new_y = self.player_body[index - 1].ycor()
           # self.player_body[index].goto(new_x, new_y)
#        self.player_body[0].forward(move_distance)

    def up(self):
        self.head.setheading(up)

    def down(self):
        self.head.setheading(down)