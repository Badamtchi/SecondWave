# lets creat a board object to represent the minesweeper game
# this is that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        #let's keep track of these parameters. they will be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board()  # plant the bombs

        # lets create the board

        # initialize a set to keep track of which locations we've uncovered
        # we will save (row, col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):


# play the game
def game(dim_size=10, num_bombs=10):
    # Step 1: creat the board and plant the bombs
    # Step 2: show the board to user and ask where the want to dig
    # Step 3: if the location is the bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is a least
    #         next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
