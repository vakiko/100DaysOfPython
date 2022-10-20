from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.color("white")
        self.speed("slowest")
        self.goto(position)
        self.setheading(90)
    def up(self):
        self.setheading(UP)
        self.forward(10)
    def down(self):
        self.setheading(DOWN)
        self.forward(10)
