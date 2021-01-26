from turtle import Turtle

player_one_position = (-80, 270)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.create_score()
        self.dash()
        self.update_scoreboard()

    def create_score(self):
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(player_one_position)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Courier", 24, "normal"))

    def dash(self):
        for idx in range(-280, 280, 4):
            self.goto(0, idx)
            self.penup()
            self.hideturtle()
            self.write("|", align="center", font=("Courier", 24, "normal"))
            self.write(" ", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))