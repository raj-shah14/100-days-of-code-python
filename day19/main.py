from turtle import Turtle, Screen
import random

screen = Screen()
screen_width = screen.window_width()
w = Turtle()
w.penup()
w.hideturtle()

def initiate_turtle(color, i):
    t = Turtle()
    t.shape('turtle')
    t.color(color)
    t.penup()
    t.goto(-screen_width/2,40*i)
    return t

def move_forward(turtles):
    for t in turtles:
        if t.xcor() < int(screen_width / 2) - 45:
            t.forward(random.randint(5,10))
    
    if any(t.xcor() >= int(screen_width / 2) - 45 for t in turtles):
        return 
    
    screen.ontimer(lambda: move_forward(turtles), 100)

def finish_line():
    l = Turtle()
    l.hideturtle()
    l.penup()
    l.goto(int(screen_width/2) - 30, 350)
    l.pendown()
    l.goto(int(screen_width/2) - 30, -250)

user_input = screen.textinput("Input Box", "Which colored Turtle is going to win the race?")

turtles = []
i = 0
for color in ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'black']:
    turtles.append(initiate_turtle(color, i))
    i += 1

finish_line()

w.goto(0, (int(screen.window_height()/2)) - 30)
w.write(f"User Predicted {user_input} to win", align='center', font=("Arial", 24, "normal"))
screen.listen()
screen.onkey(lambda: move_forward(turtles), "s")


screen.exitonclick()