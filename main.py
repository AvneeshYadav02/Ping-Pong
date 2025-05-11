from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

LEFT_POSITION=(-350,0)
RIGHT_POSITION=(350,0)
def finish():
    screen.bye()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title(titlestring="Pong")
screen.tracer(0)

l_paddle = Paddle(position=LEFT_POSITION)
r_paddle = Paddle(position=RIGHT_POSITION)

ball = Ball()
score = Score()

#Controls for both the paddles
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(finish, 'r')
screen.listen()

game_is_running = True
while game_is_running:  
    screen.update()
    time.sleep(0.01)
    
    ball.move()
    
    # Detect Ball collision with wall
    if ((ball.ycor())>290) or ((ball.ycor())<-290):
        ball.y_direction *= -1
    
    #Detect Ball collision with Paddle
    if (ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 340) or (ball.distance(l_paddle) < 50 and -330 > ball.xcor() > -340):
        ball.x_direction *= -1
        if ball.ball_speed<=2.5:    
            ball.ball_speed += 0.1
    
    #Detect when Ball goes out of bounds
    if ball.xcor()>410:
        ball.out_of_bound()
        time.sleep(0.5)
        score.l_score_up() 
        ball.ball_speed = 2
        
    elif ball.xcor()<-410:
        ball.out_of_bound()
        time.sleep(0.5)
        score.r_score_up()
        ball.ball_speed = 2
        
        

screen.exitonclick()