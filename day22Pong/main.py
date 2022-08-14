from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.title("Pong")

screen.tracer(0)
leftPaddle = Paddle((-600,0))
rightPaddle = Paddle((600,0))

leftScore = Scoreboard((-20,280))
rightScore = Scoreboard((20,280))
ball = Ball()

screen.listen()
screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")

gameOn = True

while gameOn:
    time.sleep(ball.moveSpeed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wallCollision()
        ball.move()
    if ball.distance(rightPaddle) < 40 and ball.xcor() > 320 or ball.distance(leftPaddle) < 40 and ball.xcor() < -320:
        ball.paddleCollision()
        ball.move()
        ball.move()
    if ball.xcor() > 600:
        ball.reset()
        leftScore.updateScore()
        leftScore.writeScore()
        ball.move()
    if ball.xcor() < -600:
        ball.reset()
        rightScore.updateScore()
        rightScore.writeScore()
        ball.move()
    if rightScore.score > 11 or leftScore.score > 11:
        rightScore.gameOver()
    
screen.exitonclick()
