import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # we want all players to get their move
    def get_move(self, game):
        pass

class RandomComputerPlaye(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it is invalid
            # if that spot is not available on the board, we also say it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again!')
        return val



