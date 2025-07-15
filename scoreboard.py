from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score {self.score}",False, align="Center", font=('Arial', 16, 'normal'))


    def point(self):

        self.score += 1
        self.clear()
        self.write(f"Score {self.score}",False, align="Center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",False, align="Center", font=('Arial', 24, 'normal'))


