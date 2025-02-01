import turtle

class Player:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("blue")
        self.turtle.penup()
        self.turtle.goto(0,-250)
    
    def move_up(self):
        y = self.turtle.ycor()
        self.turtle.sety(y+10)
        
    def move_down(self):
        y = self.turtle.ycor()
        self.turtle.sety(y-10)
        
    def move_left(self):
        x = self.turtle.xcor()
        self.turtle.setx(x-10)
        
    def move_right(self):
        x = self.turtle.xcor()
        self.turtle.setx(x+10)