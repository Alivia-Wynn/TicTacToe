import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for space in range(9)] #a list that creates the 3 by 3 game board
        self.current_winner = None #keeps track of the winner
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row)+ '|')

    @staticmethod
    def print_board_num():
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board: 
            print('|' + '|'.join(row)+ '|')

    def available_moves(self):
        # returns a list
        moves = []
        for (i,space) in enumerate(self.board):
            # if board looks like [x | x | o] --> (0,x) (1, x), (2,0)
            if space == ' ':
                moves.append(i) 
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_epty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, marker):
        if self.board[square] == ' ':
            self.board[square] = marker
            if self.winner(square, marker):
                self.current_winner = marker
            return True
        return False
    
    def winner(self, square, marker):
        # check to see if there is a winner in rows
        row_in = square // 3
        row = self.board[row_in*3 : (row_in +1)*3]
        if all([space == marker for space in row]):
            return True
        # check to see if there is a winner in collumns
        col_in = square % 3 
        column = [self.board[col_in + i*3]for i in range(3)]
        if all([space == marker for space in column]):
            return True
        # check to see if there is a winner on the diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(space == marker for space in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(space == marker for space in diagonal1):
                return True
        return False


    
def play(game, x_player, o_player, print_game =True):
    if print_game:
        game.print_board_num()
    marker = 'X'
    while game.empty_squares():
        # get the move from the player whos turn it is
        if marker == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, marker):
            if print_game:
                print(marker + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print( marker + ' WINS!')
                return marker

                # now we need to alternate markers
            if marker == 'X':
                marker = 'O'
            else:
                marker = 'X'
        # a short break in between turns
        time.sleep(1.0)
    if print_game:
        print('It\'s a tie...')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = ComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)