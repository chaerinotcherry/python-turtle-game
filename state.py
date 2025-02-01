import turtle
from items import Items
from obstacles import Obstacles
from score import Score
from functools import partial

class State:
    
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.level = 1
    
    def loading(self):
        loading_turtle = turtle.Turtle()
        loading_turtle.hideturtle()
        loading_turtle.color("blue")
        loading_turtle.penup()
        loading_turtle.goto(0, 0)
        loading_turtle.write("Loading...", align="center", font=("Arial", 24, "bold"))
        return loading_turtle

    def game_start(self, game_start_turtle, score=None):
        self.screen.onkey(None, "space")
        game_start_turtle.clear()
        self.screen.bgcolor("white")
        
        # Show loading text
        loading_turtle = self.loading()
        obstacles = Obstacles(self.level*5, self)  # Pass the state instance to Obstacles

        items = Items(self.level*2, self)
        if score==None:
            score = Score()
        
        # Clear loading text after preparation
        loading_turtle.clear()

        # Set up keyboard controls
        self.screen.listen()
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

        # Handle moving obstacles and checking collisions
        obstacles.move_obstacles(self.screen)
        obstacles.check_collision(self.screen, self.player, items, score)
        items.check_collision(self.screen, self.player, obstacles, score)
        
        # Set a timer for game over after 3 minutes
        self.screen.ontimer(partial(self.game_over, items), 180000)  # 180000ms == 180 seconds == 3 minutes

    def starting(self):
        game_start_turtle = turtle.Turtle()
        game_start_turtle.hideturtle()
        game_start_turtle.color("green")
        game_start_turtle.penup()
        game_start_turtle.goto(0, 0)
        game_start_turtle.write("Press 'space bar' to continue", align="center", font=("Arial", 24, "bold"))
        return game_start_turtle

    def game_clear(self, level_up_turtle):
        level_up_turtle.clear()
        
        # Display "Game Clear!" message
        game_clear_turtle = turtle.Turtle()
        game_clear_turtle.hideturtle()
        game_clear_turtle.color("white")
        game_clear_turtle.penup()
        game_clear_turtle.goto(0, 0)
        game_clear_turtle.write("Game Clear!", align="center", font=("Arial", 24, "bold"))
        
    def game_over(self, items):
        # When the game is over
        self.screen.bgcolor("orange")
        items.reset_items()

        # Display "Game Over!" message
        game_over_turtle = turtle.Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.color("black")
        game_over_turtle.penup()
        game_over_turtle.goto(0, 0)
        game_over_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))
    
    def level_up(self, obstacles, score):
        # When the player levels up
        obstacles.reset_obstacles()
        self.screen.bgcolor("yellow")
        
        # Display "Level Up!" message
        level_up_turtle = turtle.Turtle()
        level_up_turtle.hideturtle()
        level_up_turtle.color("black")
        level_up_turtle.penup()
        level_up_turtle.goto(0, 0)
        
        
        if self.level==3:
            level_up_turtle.write("Press space to see game ending!", align="center", font=("Arial", 24, "bold"))
            self.screen.onkey(partial(self.game_clear, level_up_turtle), 'space')
        else:
            level_up_turtle.write("Press space to LEVEL UP!", align="center", font=("Arial", 24, "bold"))
            self.level+=1
            self.screen.onkey(partial(self.game_start, level_up_turtle, score), 'space')
