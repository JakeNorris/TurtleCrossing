from turtle import Turtle
import random

# Initialize our constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # Create an empty list to store cars created later
        self.all_cars = []

    def create_car(self):
        # Only have a new car be created for roughly every six iterations
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Set the new car to spawn on the right side of the screen at the same x coordinate but random y coordinate
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    # Move all cars backwards because they are created on the right side of the screen
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
