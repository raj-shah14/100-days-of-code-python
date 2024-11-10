from turtle import Turtle
import random

MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed('fastest')
        self.dx = 3
        self.dy = -3

    def move(self):
        self.forward(MOVE_DISTANCE)

    def onimpact(self, left_paddle, right_paddle):

        # Move the ball
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Check for collisions with the top and bottom screen boundaries
        if self.ycor() > 290:  # Top wall
            self.sety(290)
            self.dy *= -1  # Reverse the y direction

        if self.ycor() < -290:  # Bottom wall
            self.sety(-290)
            self.dy *= -1

        # self hitting the left paddle
        if self.xcor() < -340 and (left_paddle.ycor() - 15 < self.ycor() < left_paddle.ycor() + 15):
            self.setx(-340)  # Reset position to avoid multiple collisions
            self.dx *= -1  # Reverse horizontal direction
            self.setx(self.xcor() + 30)

        # self hitting the right paddle
        if self.xcor() > 340 and (right_paddle.ycor() - 15 < self.ycor() < right_paddle.ycor() + 15):
            self.setx(340)  # Reset position to avoid multiple collisions
            self.dx *= -1  # Reverse horizontal direction
            self.setx(self.xcor() - 30)

        # Check if the self goes out of bounds (either player misses)
        if self.xcor() < -390:  # Left wall out (Player 1 misses)
            self.goto(0, 0)  # Reset the self to the center
            self.dx = random.choice([3, -3])  # Randomize initial direction

        if self.xcor() > 390:  # Right wall out (Player 2 misses)
            self.goto(0, 0)  # Reset the self to the center
            self.dx = random.choice([3, -3])  # Randomize initial direction 
        '''
        if self.heading() != RIGHT:
            self.setheading(RIGHT)
        else:
            self.setheading(LEFT)
        '''
    
    def increase_speed(self):
        self.speed(0)

    def randomize_ball_angle(self):
        self.dy = random.choice([-4, -3, 3, 4])  # Randomize vertical movement
        self.dx = -self.dx  # Reverse horizontal direction after hit

    
