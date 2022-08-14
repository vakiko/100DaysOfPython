from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def moveUp(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    def moveDown(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)
    def moveLeft(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)
    def moveRight(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
    def newLevel(self):
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
