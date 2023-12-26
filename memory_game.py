# Memory Puzzle Game Implementation
import tkinter as tk
from tkinter import messagebox
import random

class MemoryPuzzleGame:
    def __init__(self, master, rows=4, cols=4):
        # Initialization
        self.master = master
        self.master.title("Memory Puzzle Game")

        # Game Grid Configuration
        self.rows = rows
        self.cols = cols
        self.total_pairs = (rows * cols) // 2

        # Generating and Shuffling Pairs of Numbers for Tiles
        self.tiles = [i for i in range(1, self.total_pairs + 1)] * 2
        random.shuffle(self.tiles)

        # Tracking Selected Tiles and Remaining Pairs
        self.selected_tiles = []
        self.remaining_pairs = self.total_pairs

        # GUI Creation
        self.create_widgets()

    def create_widgets(self):
        # Dynamically Creating a Grid of Buttons
        self.buttons = [[tk.Button(self.master, width=8, height=4,
                                   command=lambda row=row, col=col: self.flip_tile(row, col),
                                   font=('Arial', 14, 'bold'))
                         for col in range(self.cols)] for row in range(self.rows)]

        # Placing Buttons in the Grid
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

    def flip_tile(self, row, col):
        # Handling Tile Flipping
        if len(self.selected_tiles) < 2 and not self.buttons[row][col]["state"] == tk.DISABLED:
            tile_index = row * self.cols + col
            tile_number = self.tiles[tile_index]

            # Revealing and Disabling the Selected Tile
            self.buttons[row][col].config(text=str(tile_number), state=tk.DISABLED)
            self.selected_tiles.append((row, col, tile_number))

            # Checking for Matches After Two Tiles are Selected
            if len(self.selected_tiles) == 2:
                self.master.after(1000, self.check_match)

    def check_match(self):
        # Verifying if the Selected Tiles Form a Matching Pair
        row1, col1, _ = self.selected_tiles[0]
        row2, col2, _ = self.selected_tiles[1]

        tile1_number = self.tiles[row1 * self.cols + col1]
        tile2_number = self.tiles[row2 * self.cols + col2]

        if tile1_number == tile2_number:
            # Handling Matching Pairs
            self.remaining_pairs -= 1
            if self.remaining_pairs == 0:
                # Displaying a Congratulatory Message and Closing the Application
                messagebox.showinfo("Congratulations!", "You've matched all pairs!")
                self.master.destroy()
            else:
                # Displaying a Matching Pair Message
                messagebox.showinfo("Match!", "You found a matching pair!")
        else:
            # Hiding Non-Matching Pairs
            self.buttons[row1][col1].config(text="", state=tk.NORMAL)
            self.buttons[row2][col2].config(text="", state=tk.NORMAL)

        # Resetting the Selected Tiles List
        self.selected_tiles = []

# Running the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root, rows=4, cols=4)
    root.mainloop()
