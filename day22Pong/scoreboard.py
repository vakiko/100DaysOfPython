from turtle import Turtle
FONT = ("Arial", 25, "normal")

class Scoreboard(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.write(self.score, False, align = "center", font = FONT)
    def updateScore(self):
        self.score += 1
    def writeScore(self):
        self.clear()
        self.write(self.score, False, align = "center", font = FONT)
    def gameOver(self):
        self.goto(0,0)
        self.write("Game over!", False, align = "center", font = FONT)
        