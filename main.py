from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

segments = []

#Creating first 3 segments (WhiteSnake)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")



#Snake moving forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.point()
        snake.extend()

    #Detect collision with the wall
    if snake.head.xcor() > 293 or snake.head.ycor() > 293 or snake.head.xcor() < -293 or snake.head.ycor() < -293:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False







screen.exitonclick()