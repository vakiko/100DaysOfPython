import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.moveUp, "w")
screen.onkey(player.moveDown, "s")
screen.onkey(player.moveLeft, "a")
screen.onkey(player.moveRight, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    screen.update()
    car_manager.createCar()
    car_manager.moveCars()
    
    #moves the all of the active cars
    for car in car_manager.carList:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()
    #if the player gets to the top, a new level is started
    if player.ycor() > 280:
        player.newLevel()
        scoreboard.newLevel()
        car_manager.newLevel()
screen.exitonclick()
