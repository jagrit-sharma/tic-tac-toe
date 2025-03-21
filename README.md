# Tic-Tac-Toe

A simple web-based Tic-Tac-Toe game built with JustPy, a Python framework for building interactive web applications.

## Description

This project implements a Tic-Tac-Toe game where two players can take turns to mark X and O on a 3x3 grid. It provides a real-time interactive experience using JustPy and offers features such as game reset and visual styles for X and O.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/jagrit-sharma/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the game, simply run the following command:

   ```bash
   python app.py
   ```

This will start the web server, and you can access the game in your browser at http://localhost:8000.

## Game Features
- Two-player turn-based gameplay (Player X and Player O).
- Automatically detects win or draw and displays the result.
- Reset button to restart the game.

## How It Works
1. **Game Logic**: The game is controlled by the `TicTacToe` class in `game.py`. Players take turns to make moves by clicking on the grid cells.
2. **User Interface**: The front-end is built using JustPy, which dynamically updates the board as players make moves.
3. **Grid**: The board is a 3x3 grid of clickable buttons. Players click on the grid to place their marks (X or O).
4. **Reset**: There is a reset button that clears the board and starts a new game.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](https://github.com/jagrit-sharma/tic-tac-toe/blob/main/LICENSE).

## Contact

Jagrit Sharma - sharma.jagrit.1899@gmail.com