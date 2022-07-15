"""Turtle-Crossing Game : The player control the turtle which can only move forward, where there are a bunch of randomly generated cars
which are going horizontally across the screen. If the player reaches the end of screen, the turtle will back to
the starting point and the car speed increases. Create class, inheritance of class, object inside the class,
turtle coordinate system, turtle game engine. """


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()

player = Player()

score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # When the turtle collide with the car
    for any_car in car.car_manager:
        if player.distance(any_car) < 25:
            game_is_on = False
            score.game_over()

    # When the turtle able to reach finish line
    if player.ycor() > 290:
        player.restart()
        score.increase_level()
        car.increase_speed()

screen.exitonclick()
