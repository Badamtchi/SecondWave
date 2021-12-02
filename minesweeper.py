import random
import re

# lets creat a board object to represent the minesweeper game
# this is that we can just say "create a new board object", or
# "dig here", or "render this game for this object"


class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they will be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board()  # plant the bombs
        self.assign_value_to_borad()

        # lets create the board

        # initialize a set to keep track of which locations we've uncovered
        # we will save (row, col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] in range(self.dim_size)]

        # plant a bomb
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size   # we want the remainder to tell us what index in that row to locate

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1
        return board

    def assign_value_to_borad(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it will save us
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # if this is already a bomb, we don't want to calculate anything
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at the location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish digging
        # dig at location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row, col))  # keeping track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.borad[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)
        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it will print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array the represent what the use would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_bord[row][col] = str(self.board[row][col])
                else:
                    visible_bord[row][col] = ' '
        # put this together in a string
# play the game


def play(dim_size=10, num_bombs=10):
    # Step 1: creat the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the board to user and ask where the want to dig
    # Step 3: if the location is the bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is a least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as roe,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print('Invalid location. Try again...')
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhhhh
            break # game over rip

    # 2 ways to end loop, let's check which one
    if safe:
        print('CONGRATULATIONS!!!! YOU ARE VICTORIES!!')
    else:
        print('SORRY!!! GAME OVER!')
        # let's reveal the whole board!
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == "__main__":
    play()
