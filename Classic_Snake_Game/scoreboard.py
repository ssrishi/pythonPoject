from turtle import Turtle
ALIGN = "center"
FONT = ('courier', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)
        with open("data.txt", mode='w') as file:
            file.write(str(self.high_score))


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0 
        self.score_update()     

    def increase_score(self):
        self.score += 1
        self.score_update()
