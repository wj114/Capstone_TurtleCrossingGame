from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager():

    def __init__(self):
        self.car_manager = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dice = random.randint(1, 6)
        if dice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(f"{random.choice(COLORS)}")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(290, random.randint(-250, 250))
            self.car_manager.append(new_car)

    def move(self):
        for car in self.car_manager:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
