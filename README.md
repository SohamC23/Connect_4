# Connect_4

Python code to play the game Connect 4 against a custom bot

## About

This project is a Python implementation of Connect 4 where a human player plays against a bot built with custom game logic. The game runs in the console, lets the player choose whether to go first or second, and updates the board after each move

The bot does more than pick random moves. It checks for winning moves, blocks the player’s threats, avoids risky positions, and looks for patterns that can improve its chances of winning

## Features

- Play Connect 4 against a custom Python bot
- Choose to go first or second
- Console-based board display with move-by-move updates
- Input validation for invalid or full columns
- Win detection for vertical, horizontal, and diagonal lines
- Bot logic that can:
  - Complete its own 4-in-a-row
  - Block the player’s 4-in-a-row
  - Look for open and closed two- and three-piece patterns
  - Avoid moves that create easy wins for the opponent

## Technologies Used

- Python
- `random`
- `time`
- `IPython.display.clear_output`

## How It Works

The game stores the visible board in one matrix and uses a separate logic matrix to evaluate moves and detect patterns. The player enters a column number, and the program places the piece in the next available row in that column

The bot then analyzes the board and selects a move based on priority rules such as:
1. Make a winning move if possible
2. Block the player from winning
3. Avoid dangerous moves
4. Build stronger future positions

## Project Highlights

- Built a full playable Connect 4 game in Python
- Created a custom bot using rule-based decision logic instead of advanced AI or neural networks
- Implemented board-state checking for wins in all directions
- Added move validation and game-end handling for wins and ties
- Structured the game with functions for board printing, move placement, win checks, and bot strategy

## What I Learned

Through this project, I strengthened my skills in:

- Python programming
- Game logic design
- Conditional logic
- Matrix-based board representation
- Debugging and testing
- Breaking a large problem into smaller functions

## Future Improvements

- Improve the bot against more advanced player strategies
- Add a graphical interface
- Refactor the code for readability and modularity
- Add difficulty levels
- Explore Minimax or other search-based algorithms for stronger gameplay

## Running the Project

Clone the repository:

```bash
git clone https://github.com/SohamC23/Connect_4.git
cd Connect_4
```

## License

This project uses the Apache License 2.0
