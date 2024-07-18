from scoreboard import ScoreBoard
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import random
import time

random_color = (100, random.randint(140, 150), random.randint(230, 255))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

score = ScoreBoard()
score_count = 0
high_score = 0
snake = Snake(random_color)
food = Food(random_color)

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

border = Turtle()
border.color('white')
border.shape('square')
border.shapesize(0.1, 200)
border.penup()
border.goto(0, 255)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        snake.extend(random_color)
        random_color = (100, random.randint(75, 150), random.randint(185, 255))
        food.refresh(random_color)
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 255 or snake.head.ycor() < -290:
        snake.reset(random_color)
        food.refresh(random_color)
        score.reset()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            snake.reset(random_color)
            food.refresh(random_color)
            score.reset()


screen.exitonclick()



