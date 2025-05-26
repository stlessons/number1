# TETRIS Game

This is a simple implementation of the classic TETRIS game using Python and Pygame.

## Project Structure

```
tetris-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game
│   │   ├── __init__.py  # Game package initialization
│   │   ├── board.py     # Manages the game board
│   │   ├── tetromino.py  # Represents TETRIS shapes
│   │   └── utils.py     # Utility functions for game logic
│   └── assets
│       └── __init__.py  # Assets package initialization
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To run this project, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tetris-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run the following command:
```
python src/main.py
```

Enjoy playing TETRIS!