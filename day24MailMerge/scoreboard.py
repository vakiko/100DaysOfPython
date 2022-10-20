from turtle import Turtle
FONT = ("Arial", 15, "normal")
import time
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("highscores.txt") as data:
            self.highscore = int(data.read())
        self.goto(0,270)
        self.color("white")
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align = "center", font = FONT)
    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align = "center", font = ("Arial", 15, "normal"))
    def gameOver(self):  
        self.goto(0,0)
        self.write("Game over!", False, align = "center", font = FONT)
        if self.score > self.highscore:
            with open("highscores.txt", mode="w") as data:
                data.write(str(self.score))
            self.highscore = self.score
        time.sleep(0.5)
        self.clear()
        self.score = 0
        self.goto(0,270)
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align = "center", font = FONT)
        