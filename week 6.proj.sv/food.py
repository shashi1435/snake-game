
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        # Generate a random position for the food that is within the screen boundaries
        x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return (x, y)