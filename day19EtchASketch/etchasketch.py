from turtle import Turtle, Screen

clay = Turtle()
clay.shape("turtle")

def moveForward():
    clay.forward(10)
    
def moveBackward():
    clay.backward(10)
    
def turnLeft():
    newHead = clay.heading() + 10
    clay.setheading(newHead)
    
def turnRight():
    newHead = clay.heading() - 10
    clay.setheading(newHead)
    
def clear():
    clay.clear()
    clay.penup()
    clay.home()
    clay.pendown()

screen = Screen()

screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "b")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight, "d")
screen.onkey(clear, "c")


screen.exitonclick()

