from turtle import Turtle
startingPositions = [(0, 0), (-20, 0), (-40, 0)]
moveDistance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
import time

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in startingPositions:
            self.addSegment(position)
    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)
        
    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.head.forward(moveDistance)
    
    def collision(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            if self.segments[segNum].distance(self.head) < 15:
                return True
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        time.sleep(0.5)
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
