from turtle import Turtle
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.write(f"Score = {self.score}", False, align = "center", font = FONT)
    def updateScore(self):
        self.score += 1
    def writeScore(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align = "center", font = ("Arial", 15, "normal"))
    def gameOver(self):
        self.goto(0,0)
        self.write("Game over!", False, align = "center", font = FONT)
        