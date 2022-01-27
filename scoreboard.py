from turtle import Turtle

# Initialize our constants
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    # Clear old scoreboard and write the current level at the top left of screen
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase level and call update_scoreboard method
    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    # Bring turtle to center screen and alert user the game has ended
    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
