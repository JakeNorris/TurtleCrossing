import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen to meet our requirements
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor("white")

# Initialize the player, scoreboard, and car_manager objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Tell screen to listen for the up arrow key to move player forward
screen.listen()
screen.onkey(player.move_forward, "Up")

# While loop to keep game functioning until GAME OVER
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check each car for distance from player, if close enough end game
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

    # When player successfully reaches the other side advance level and bring back to start
    if player.ycor() > 270:
        player.start_position()
        scoreboard.next_level()

    # Every iteration through the while loop move current cars forward and create a new car
    # Remember this will only create a new car when the randint == 1
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()
