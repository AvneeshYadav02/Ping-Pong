from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.create_score()
        
    def create_score(self):    
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x= 0,y =250)
        self.write(arg=f"{self.l_score}|{self.r_score}" ,align=ALIGNMENT, font=FONT)
    
    def l_score_up(self):
        self.clear()
        self.l_score += 1
        self.create_score()
        
    def r_score_up(self):
        self.clear()
        self.r_score += 1
        self.create_score()