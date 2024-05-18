
from constants import GRID_SIZE

class Snake:
    def __init__(self):
        self.body = [(GRID_SIZE, GRID_SIZE)]  # Start with a single segment at a specific position
        self.direction = "RIGHT"  # Initial direction

    def move(self):
        # Move the snake by adding a new segment in the current direction
        head = self.body[0]
        x, y = head
        if self.direction == "UP":
            self.body.insert(0, (x, y - GRID_SIZE))
        elif self.direction == "DOWN":
            self.body.insert(0, (x, y + GRID_SIZE))
        elif self.direction == "LEFT":
            self.body.insert(0, (x - GRID_SIZE, y))
        elif self.direction == "RIGHT":
            self.body.insert(0, (x + GRID_SIZE, y))
        self.body.pop()  # Remove the last segment to keep the snake the same length

    def change_direction(self, direction):
        # Change the snake's direction, but prevent it from moving back on itself
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def grow(self):
        # Add a new segment to the end of the snake
        self.body.append(self.body[-1])