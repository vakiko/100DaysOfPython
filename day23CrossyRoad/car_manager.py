COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:
    
    def __init__(self):
        super().__init__()
        self.carList = []
        self.createCar()
        self.moveSpeed = STARTING_MOVE_DISTANCE
    def createCar(self):
        if random.randint(1,6) == 5:
            newCar = Turtle("square")
            newCar.penup()
            newCar.shapesize(stretch_wid = 1, stretch_len = 2)
            newCar.color(random.choice(COLORS))
            newCar.goto(300,random.randint(-260,260))
            newCar.setheading(180)
            self.carList.append(newCar)
    def moveCars(self):
        for car in self.carList:
            car.forward(self.moveSpeed)
    def newLevel(self):
        self.moveSpeed += MOVE_INCREMENT
        
        
