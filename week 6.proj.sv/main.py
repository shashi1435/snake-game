
import tkinter as tk
import os
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

def main():
    root = tk.Tk()
    root.title("Snake Game")

    canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
    canvas.pack()

    game = None

    def start_game():
        nonlocal game
        game = Game(canvas)
        update_game()

    def end_game():
        nonlocal game
        if game:
            game_over_text = f"Game Over! Score: {game.score}"
            if game.score > high_score:
                high_score_text = f"New High Score: {game.score}"
                high_score_label.config(text=high_score_text)
                save_high_score(game.score)
            canvas.create_text(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                text=game_over_text,
                fill="white",
                font=("Helvetica", 24),
            )
            game = None

    def update_game():
        if game and game.update():
            game.draw()
            root.after(100, update_game)
        elif game:
            end_game()

    def load_high_score():
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                return int(file.read())
        else:
            return 0

    def save_high_score(score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

    high_score = load_high_score()  # Load the high score from file

    start_button = tk.Button(root, text="Start Game", command=start_game)
    start_button.pack()

    end_button = tk.Button(root, text="End Game", command=end_game)
    end_button.pack()

    high_score_label = tk.Label(root, text=f"High Score: {high_score}", fg="white", bg="black")
    high_score_label.pack()

    def on_key_press(event):
        # Handle keyboard input to change the snake's direction
        key = event.keysym
        if key == "Up":
            game.snake.change_direction("UP")
        elif key == "Down":
            game.snake.change_direction("DOWN")
        elif key == "Left":
            game.snake.change_direction("LEFT")
        elif key == "Right":
            game.snake.change_direction("RIGHT")

    root.after(100, update_game)  # Start the game loop
    root.bind("<KeyPress>", on_key_press)  # Bind keyboard events
    root.mainloop()

if __name__ == "__main__":
    main()