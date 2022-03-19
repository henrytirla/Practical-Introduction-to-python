'''
(a) Write a class called Connect4 that implements the logic of a Connect4 game. Use the
Tic_tac_toe class from this chapter as a starting point.
(b) Use the Connect4 class to create a simple text-based version of the game.
'''

import pprint as pp
class ConnectFour:

    def __init__(self):

        self.Board = [[' ' for i in range(7)] for i in range(6)]

    def get_diag_and_row(self):
        ''' to get rows,columns and diagonals'''
        # To print the board from a negative axis
        x1 = [[i[j] for j in range(-1, -(len(i)+1), -1)]for i in self.Board]
        
        def diag(d):
            ''' To get diagonals for the positive and negative slope '''

            neg = [[d[i][j] for i in range(k+1) for j in range(k, -1, -1) if i+j == k-1]
                    for k in range(1, 7)]
            pos = [[d[i][j] for i in range(5, -1, -1) for j in range(-1, -8, -1) if i+j == k]
                    for k in range(6, -2, -1)]
            c = [i for i in (neg+pos) if len(i) >= 4]

            return c

        check_list = (diag(x1) + diag(self.Board) + self.Board)

        return check_list

    def get_column(self, col_index):
        """
        Returns a value at that index on every row 

        """
        return [i[col_index] for i in self.Board]

    def check_win(self):
        """
        checks for four_in_a_row in the positive and Negative diagonals  

        Returns
        -------
        the True if there is four in a row

        """
        #check diagonals and rows
        four_in_row = [['1' for i in range(4)], ['2' for i in range(4)]]

        for check in self.get_diag_and_row():

            for j in range(len(check)):

                if check[j:j+4] in four_in_row and j < len(check) - 3:
                    #print ('yes')
                    return True
        #Check columns
        for i in range(7):
            for j in range(6 - 3):
                if self.get_column(i)[j:j + 4] in four_in_row:
                    return True

        else:
            return False

    def make_move(self, col, player):
        """
        Parameters
        ----------
        col : int.
        player : player 1 and 2.
        
        Returns
        -------
          The Board with the players move registered.
        """
        u = -1
        while self.Board[u][col] != ' ' and u != -6:
            u -= 1

        self.Board[u][col] = player
        pp.pprint(self.Board)
        return self.Board

    def play(self):
        """
        To play the Connect4 game  
        -------
        Returns
        The winner of the game after each player makes their moves.
        """
        pp.pprint(self.Board)
        for i in range(42):
            #pp.pprint(self.Board)
            
            col = int(input('Enter column: '))-1
            self.make_move(col, '1')
            if self.check_win() is True:

                return 'Player 1 Wins\nTHANKS FOR PLAYING'

                break

            col = int(input('Enter column: '))-1
            self.make_move(col, '2')
            if self.check_win() is True:

                return 'Player 2 Wins\nTHANKS FOR PLAYING'

                break


game = ConnectFour()
print(game.play())
