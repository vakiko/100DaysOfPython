FONT = ("Courier", 24, "normal")
from turtle import Turtle
STARTING_POSITION = -280,280
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(STARTING_POSITION)
        self.color("black")
        self.write(f"Level {self.level}", False, align = "center", font = FONT)
    def newLevel(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, align = "center", font = FONT)
    def gameOver(self):
        self.goto(0,0)
        self.write("Game over!", False, align = "center", font = FONT)   
