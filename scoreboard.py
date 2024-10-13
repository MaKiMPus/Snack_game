from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.highscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 325)
        self.write(f"Score = {self.score}  High Score = {self.highscore}", align=ALIGNMENT, font=FRONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over!, you've got {self.score} score.", align=ALIGNMENT, font=FRONT)

    def increas_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
