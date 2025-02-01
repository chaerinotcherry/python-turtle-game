import random
import turtle
from functools import partial
from game_clear import game_clear
from level_up import level_up

class Items:
    def __init__(self, num, state):
        self.items = []
        self.state = state
        for _ in range(num):
            self.create_item()
            
    def create_item(self):
        # Create an item (yellow circle) at a random position
        item = turtle.Turtle()
        item.color("yellow")
        item.shape("circle")
        item.penup()
        item.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.items.append(item)
    
    # Update inside the Items class where collision occurs
    def check_collision(self, screen, player, obstacles, score):
        for item in self.items:
            if player.turtle.distance(item) < 20:
                item.hideturtle()
                self.items.remove(item)
                score.increase_score(5)
                score.update_score_display()

                # Level up when all items are collected
                if len(self.items) == 0:
                    self.state.level_up(obstacles, score)  # Ensure you have access to the state instance
        screen.ontimer(partial(self.check_collision, screen, player, obstacles, score), 100)

    
    def get_items(self):
        return self.items
    
    def reset_items(self):
        # Hide all items and clear the list
        for item in self.items:
            item.hideturtle()
        self.items = []  # Reset the list of items

