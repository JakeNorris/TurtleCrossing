from turtle import Turtle

# Initialize our constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 11
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.start_position()

    # Brings player back to the bottom of screen start position
    def start_position(self):
        self.goto(STARTING_POSITION)

    # Keep player on the same x coordinate and move up the y-axis
    def move_forward(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
