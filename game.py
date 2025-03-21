class TicTacToe:
    def __init__(self, size=3):
        self.n = size
        self.board = [['_' for _ in range(self.n)] for _ in range(self.n)]
        self.currPlayer = 'X'
        self.gameOver = False

    def isValid(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n and self.board[row][col] == '_'

    def isWinner(self, player):
        for i in range(self.n):
            if all(self.board[i][j] == player for j in range(self.n)):  # Row check
                return True
            if all(self.board[j][i] == player for j in range(self.n)):  # Column check
                return True
        if all(self.board[i][i] == player for i in range(self.n)):  # Main diagonal
            return True
        if all(self.board[i][self.n - 1 - i] == player for i in range(self.n)):  # Anti-diagonal
            return True
        return False

    def isDraw(self):
        for row in self.board:
            if '_' in row:
                return False
        return True

    def makeMove(self, row, col):
        """Handles a player's move"""

        if self.gameOver:  # Prevent moves if the game is over
            return {"status": "invalid", "message": "Game over! Please reset to play again."}

        if not self.isValid(row, col):
            return {"status": "invalid", "message": "Invalid move! Cell occupied or out of bounds."}

        self.board[row][col] = self.currPlayer

        if self.isWinner(self.currPlayer):
            self.gameOver=True
            return {"status": "win", "message": f"Player {self.currPlayer} wins!"}

        if self.isDraw():
            self.gameOver=True
            return {"status": "draw", "message": "It's a draw!"}

        self.currPlayer = 'O' if self.currPlayer == 'X' else 'X'
        return {"status": "continue", "message": f"Player {self.currPlayer}'s turn"}

    def resetGame(self):
        """Resets the game"""
        self.board = [['_' for _ in range(self.n)] for _ in range(self.n)]
        self.currPlayer = 'X'
        self.gameOver=False
        return {"status": "reset", "message": "Game reset!"}