from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_speed = 2
        self.x_direction = 1
        self.y_direction = 1

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.color('white')
        
    def move(self):
        new_x = self.xcor() + self.x_direction * self.ball_speed
        new_y = self.ycor() + self.y_direction * self.ball_speed
        self.goto(x= new_x ,y= new_y)
        
    def out_of_bound(self):
        self.hideturtle()
        self.x_direction *= -1
        self.goto(0,0)
        self.showturtle()