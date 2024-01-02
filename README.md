# Memory Puzzle Game Implementation

**Welcome to the Memory Puzzle Game!**

## Overview

This implementation brings the classic Memory Puzzle Game to life using Python's Tkinter library. Test and enhance your memory skills by finding matching pairs hidden behind the tiles. This README provides an overview of how to play, key features, and how to run the game.

## How to Play

1. **Launch the Game:**
   - Run the Python script (`MemoryPuzzleGame.py`) to start the game.

2. **Game Interface:**
   - A grid of buttons will appear, each representing a tile in the memory puzzle.

3. **Reveal Tiles:**
   - Click on a tile to reveal its number.
   - Click on another tile to reveal its number.

4. **Matching Pairs:**
   - If the numbers match, the pair remains revealed.
   - If the numbers don't match, the tiles are hidden again.

5. **Winning Condition:**
   - Continue matching pairs until all pairs are found.
   - Upon winning, a congratulatory message is displayed.

6. **Customization:**
   - Adjust the number of rows and columns in the `MemoryPuzzleGame` instantiation for a customized experience.

## Implementation Details

- **Grid Configuration:**
  - The game grid is dynamically generated with a specified number of rows and columns.

- **Tile Numbers:**
  - Pairs of numbers are generated, shuffled, and assigned to tiles on the grid.

- **Button Interface:**
  - Tkinter buttons create the game interface, each associated with a specific tile.

- **Flipping Tiles:**
  - Clicking on a button reveals the associated tile's number. The game allows revealing two tiles at a time.

- **Matching Pairs:**
  - The game checks if the numbers on the selected tiles match. If they do, the pair remains revealed; otherwise, the tiles are hidden again.

- **Winning Condition:**
  - The game concludes when all pairs have been successfully matched, displaying a congratulatory message.

## Running the Game

1. **Prerequisites:**
   - Ensure you have Python installed on your system.

2. **Launch the Game:**
   - Run the provided Python script (`MemoryPuzzleGame.py`).
   - The game window will appear, and you can start playing!

## Contribution

Feel free to customize the game or contribute to the project by submitting pull requests.

**Have fun challenging your memory with the Memory Puzzle Game!**
