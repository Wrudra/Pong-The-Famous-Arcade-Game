from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Scoreboard setup
scoreboard = Scoreboard()

# Create and move a paddle
r_paddle = Paddle((350, 0))     # Tuple passing coordinate
l_paddle = Paddle((-350, 0))

# Create a ball
ball = Ball()

# Movement commands
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:     # Removing the goto animation, screen.tracer(0)
  screen.update()
  ball.move()     # Ball moving while screen refresh
  
  # Detect collision with wall and bounce
  if ball.ycor() > 285 or ball.ycor() < -285:     # Then it needs to bounce
    ball.y_bounce()
  
  # Detect collision with r_paddle and l_paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    ball.x_bounce()

  # Detect when r_paddle misses the ball
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  # Detect when l_paddle misses the ball
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()


screen.exitonclick()