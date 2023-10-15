from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)
    
    def create_paddle(self, x, y):
       self.shape("square")
       self.color('white')
       self.shapesize(stretch_wid=5, stretch_len=1)
       self.penup()
       self.goto(x, y)
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)    
