import turtle
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('ArcadeClassic', 20, 'normal')
FONT_ALT = ('ArcadeClassic', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            _ = int(file.read())
            print(_)
        self.high_score = _
        self.color('White')
        self.hideturtle()
        self.goto(0, 267)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}      High Score:  {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over.", move=False, align=ALIGNMENT, font=FONT_ALT)
