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
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

    
