import turtle as t
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import time

# Screen 
win = t.Screen()
win.setup(width=600, height=600)
win.bgcolor("black")
win.title("Snake Game")
win.tracer(0)

# Calling all the Classes
snake = Snake()
food = Food()
score = Scoreboard()


# ON Key Press 
win.listen()
win.onkey(snake.up, "Up")
win.onkey(snake.down, "Down")
win.onkey(snake.right, "Right")
win.onkey(snake.left, "Left")


game_on = True

while game_on:
    win.update()
    time.sleep(.1)
    snake.move()
    
    
    # Detect Collsion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    
    # Detect Collsion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()


    # Detect Collsion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()



win.exitonclick()