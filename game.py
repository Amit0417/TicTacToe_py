class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use list for our 3x3 board
        self.current_winner = None # Keep tracking winner