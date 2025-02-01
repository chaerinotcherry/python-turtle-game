from functools import partial
import turtle
from player import Player
from state import State  # No need to import game_start, starting directly

# Setup the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Initialize player and state
player = Player()
state = State(screen, player)

# Show the starting screen with the instruction
game_start_turtle = state.starting()

# Listen for keypress and trigger game start
screen.listen()
screen.onkey(partial(state.game_start, game_start_turtle), 'space')  # No need to pass game_start_turtle here

# Start the main game loop
screen.mainloop()
