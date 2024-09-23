from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_move = 0.1
    self.y_move = 0.1
    
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
  
  def y_bounce(self):
    self.y_move *= -1     # If the ball is in +y, then after bounce -y

  def x_bounce(self):
    self.x_move *= -1
  
  def reset_position(self):
    self.goto(0, 0)     # When the ball passes beyond x border, 
    self.x_bounce()     #the ball will reset and the other player will recieve the ball

    
         

    
