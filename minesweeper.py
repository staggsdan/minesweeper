import random

# need to create a board Object to represent the game board
# this is her to say "create a new board (object)" or "dig here" or "render this"
class Board:
    def __init__(self, dim_size, num_bombs):
        # track params
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        # create  board
        self.board = self.make_new_board()
        # initialize a set to track coords we've unconvered
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        # makes a new board based on dim size and num bombs. could store info many ways, but list of lists works
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
            # meaning if we've already planted a bomb (star) at this location, move on.
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
#         need to iterate through up to 8 positions next to each grid spot, but don't go out of bounds
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) +1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) +1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1




# play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create a board and plant the bombs
    # step 2: show the user the board and ask for their dig location
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until we are in proximity of a bomb
    # step 4: repeat 2 and 3