"""
Create snake body
Move Snake
Create Snake Food
Detect collision with food
Create scoreboard
Detect collision with wall
Detect collision with tail
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from playsound import playsound
import multiprocessing


def start_game(screen, snake, food, score, p):
    game_on = True

    sleep_number = 0.1

    while game_on:
        screen.update()
        time.sleep(sleep_number)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.create_segment()
            score.update_score()
            sleep_number -= 0.005

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_on = False
            score.game_over()
            p.terminate()
            screen.exitonclick()

        # Detect collision with tail
        # If head collides with any segment in taol trigger game_over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()
                p.terminate()
                screen.exitonclick()


def main():
    screen = Screen()

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.tracer(0)

    p = multiprocessing.Process(target=playsound, args=("audio.mp3",))
    p.start()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()

    start_game(screen, snake, food, score, p)


if __name__ == "__main__":
    main()
