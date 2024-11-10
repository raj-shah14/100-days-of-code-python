from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Ping Pong Game")
screen.tracer(0)

p1 = Paddle((-370,0))
p2 = Paddle((380,0))
ball = Ball()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if p1.distance(ball) <= 15:
        ball.onimpact(p1, p2)
    if p2.distance(ball) <= 15:
        ball.onimpact(p1, p2)

screen.exitonclick()