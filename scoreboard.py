from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.reading_highscore()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,250)
        self.write(f"Score {self.score}   High score {self.reading_highscore()}",False, align="Center", font=('Arial', 16, 'normal'))


    def point(self):
        self.score += 1
        self.clear()

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.saving_highscore()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}   High score {self.high_score}",False, align="Center", font=('Arial', 16, 'normal'))

    def reset_score(self):
        self.score = 0

    def saving_highscore(self):
        with open("data.txt","w") as data:
            x = data.write(str(self.high_score))
            print(f"High score = {self.high_score}")

    def reading_highscore(self):
        with open("data.txt") as data:
            y = data.read()
            return int(y)









    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",False, align="Center", font=('Arial', 24, 'normal'))


