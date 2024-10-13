from turtle import Turtle, Screen
from snack import Snack
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("SNACK GAME")
screen.tracer(0)

snack = Snack()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snack.up, "w")
screen.onkey(snack.down, "s")
screen.onkey(snack.left, "a")
screen.onkey(snack.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()

    #Detect collisions with food
    if snack.head.distance(food) < 15:
        food.refresh_location()
        scoreboard.increas_score()
        snack.extend()

    #Detect collision with the wall
    if snack.head.xcor() > 335 or snack.head.xcor() < -335 or snack.head.ycor() > 335 or snack.head.ycor() < -335:
        # game_is_on = False
        # scoreboard.game_over()
        snack.reset()
        scoreboard.reset()
        
        

    #Detect collision with snack's tail == any segment of snack
    # for segment in snack.segments[1:-1]:
    #     if segment != snack.head:
    #         if snack.head.distance(segment) < 1:
    #             game_is_on = False
    #             scoreboard.game_over()
    for segment in snack.segments[1:-1]:
        if snack.head.distance(segment) < 1:
            # game_is_on = False
            # scoreboard.game_over()
            snack.reset()
            scoreboard.reset()
            
            


screen.exitonclick()