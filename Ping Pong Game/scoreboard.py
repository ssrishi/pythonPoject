from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=('arial', 24, 'bold'))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=('arial', 24, 'bold'))


    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()


