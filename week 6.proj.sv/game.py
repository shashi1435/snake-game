
import tkinter as tk
from snake import Snake
from food import Food
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def draw(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the snake
        for segment in self.snake.body:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green")

        # Draw the food
        x, y = self.food.position
        self.canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="red")

        # Update the score
        self.canvas.create_text(10, 10, anchor="nw", text=f"Score: {self.score}", fill="white")

    def check_collision(self):
        # Check if the snake has collided with itself or with the screen boundaries
        head = self.snake.body[0]
        if (
            head[0] < 0
            or head[0] >= SCREEN_WIDTH
            or head[1] < 0
            or head[1] >= SCREEN_HEIGHT
            or len(self.snake.body) != len(set(self.snake.body))
        ):
            return True
        return False

    def update(self):
        # Move the snake
        self.snake.move()

        # Check for collisions
        if self.check_collision():
            print("Game over!")
            return False

        # Check if the snake has eaten the food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()  # Grow the snake
            self.food.position = self.food.generate_food_position()  # Generate new food
            self.score += 1

        return True