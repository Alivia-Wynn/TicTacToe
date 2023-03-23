import math
import random

class Player:
    def __init__(self, marker):
        # marker is the x or o
        self.marker = marker
    # all players will be given a turn
    def get_move(self, game):
        pass
class ComputerPlayer(Player):
    def __init__(self, marker):
        super().__init__(marker)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, marker):
        super().__init__(marker)
    def get_move(self, game):
        valid_square = False
        val = None
        while valid_square is False:
            square = input(self.marker + '\'s turn. Choose a space between 0 and 8:')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input. Try again')
        return val