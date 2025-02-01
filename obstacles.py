import random
import turtle
from functools import partial

class Obstacles:
    def __init__(self, num, state):  # Add state parameter
        self.state = state  # Store state instance
        self.obstacles = []
        for _ in range(num):
            self.create_obstacle()
            
    def create_obstacle(self):
        # Create an obstacle at a random location
        obstacle = turtle.Turtle()
        obstacle.color("red")
        obstacle.penup()
        obstacle.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.obstacles.append(obstacle)
        
    def move_obstacles(self, screen):
        # Move obstacles to new random locations
        for obstacle in self.obstacles:
            obstacle.goto(random.randint(-250, 250), random.randint(-250, 250))
        # Call the function repeatedly using screen.ontimer()
        screen.ontimer(partial(self.move_obstacles, screen), 100)
    
                        
    def reset_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.hideturtle()
        self.obstacles = []  # Clear the obstacle list

    # Update the check_collision method in Obstacles to call game_over from State
    def check_collision(self, screen, player, items, score):
        for obstacle in self.obstacles:
            if player.turtle.distance(obstacle) < 20:
                print("Collision detected!")
                score.decrease_score(10)
                score.update_score_display()
            if score.get_score() < -50:
                # Reset obstacles and trigger game over
                self.reset_obstacles()

                # Optionally call game_over here from State
                screen.bgcolor("orange")  # Immediate feedback on collision
                items.reset_items()  # Optionally reset items as well

                # Example: Trigger game over after collision (this would now use the game_over method in State)
                self.state.game_over(items)  # Assuming state is an instance of State class
        screen.ontimer(partial(self.check_collision, screen, player, items, score), 100)

    def get_obstacles(self):
        return self.obstacles
