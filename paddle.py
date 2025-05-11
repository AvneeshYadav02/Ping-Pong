from turtle import Turtle

SPEED = 25

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()
    
    def create_paddle(self):
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(self.position)
         

    def go_up(self):
        self.sety(self.ycor()+SPEED)
            
    def go_down(self):
        self.sety(self.ycor()-SPEED)
