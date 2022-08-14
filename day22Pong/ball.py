from turtle import Turtle
trajectory = 1
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(0,0)
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.penup()
        self.goto(newX, newY)
    def wallCollision(self):
        self.yMove *= -1
    def paddleCollision(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9
        
    def reset(self):
        self.clear()
        self.goto(0,0)
        self.paddleCollision()
        self.moveSpeed = 0.1