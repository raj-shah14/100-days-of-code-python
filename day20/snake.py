from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for p in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(p)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            last_ele = self.segments[seg_num -1]
            new_x, new_y = last_ele.xcor(), last_ele.ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)
    
    def down(self):
        self.head.setheading(DOWN)
    
    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)
