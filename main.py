from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
y = 0
x = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()
s.listen()
s.onkey(snake.up , "Up")
s.onkey(snake.down , "Down")
s.onkey(snake.left , "Left")
s.onkey(snake.right ,"Right")



game_is_on = True
while game_is_on:
    # s.update()
    # time.sleep(0.1)
    snake.move()
    s.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_segment()
        s.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.save_highscore()
            scoreboard.reset()


s.exitonclick()
