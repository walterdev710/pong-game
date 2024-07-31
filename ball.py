from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.1
        self.x_coordinates = 10
        self.y_coordinates = 10
    
    def move(self):
        new_x = self.xcor() + self.x_coordinates
        new_y = self.ycor() + self.y_coordinates
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_coordinates *=-1
        
    def bounce_x(self):
        self.x_coordinates *=-1
        self.move_speed *=0.9
    
        
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        
    def increase_speed(self):
        self.speed(0)