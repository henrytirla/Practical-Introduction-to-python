"""
Write a text-based version of the game Memory. The game should generate a 5 × 5 board (see
the exercise from Chapter 8). Initially the program should display the board as a 5 × 5 grid of
asterisks. The user then enters the coordinates of a cell. The program should display the grid
with the character at those coordinates now displayed. The user then enters coordinates of
another cell. The program should now display the grid with the previous character and the
new character displayed. If the two characters match, then they should permanently replace
the asterisks in those locations. Otherwise, when the user enters the next set of coordinates,
those characters should be replaced by asterisks. The game continues this way until the player
matches everything or runs out of turns. You can decide how many turns they player gets.
"""

from string import ascii_lowercase
from random import sample, shuffle
from pprint import pprint
import numpy as np
from sys import exit

COOR = [0,1,2,3]

def create_board():
    # From string module, imported all corresponding characters and grouped them together in source variable.
    source = ascii_lowercase
    
    # Using sample function from random module, grabbed 18 random characters from source string.
    # After which, the random chars cloned to create pairs for memory game. 
    # Note, sample returns a list.
    chars = sample(source, 8) * 2
    
    # Used shuffle function to randomize the list of characters
    shuffle(chars)
    
    # Used numpy instead of list comprehensions to create an array of the chars at a 4x4 size.
    # After which, the array was converted to a list using the .tolist() method.
    L = np.array(chars).reshape(4,4).tolist()
    return L

def create_asterisks_board(board):
    M = [['*' for coulmn in row] for row in board]
    return M

def game_on(board, asterisks_board):
    pprint(asterisks_board)
    pprint(board) # DELETE LATER
    N = 10
    while N > 0:
        user_coor_1 = get_coor()
        print(f'\nFirst set of coordinates are {user_coor_1}.\n')
        print(board[user_coor_1[0]][user_coor_1[1]])
        user_coor_2 = get_coor()
        print(f'\nSecond set of coordinates are {user_coor_2}.\n')
        print(board[user_coor_2[0]][user_coor_2[1]])
        asterisks_board, N = check_coors(user_coor_1, user_coor_2, board, asterisks_board, N)
        win_lose_check(board, asterisks_board, N)
        pprint(asterisks_board)
    
def get_coor():
    message = 'Enter row: '
    row = validate_coor(message, COOR)
    message = 'Enter column: '
    column = validate_coor(message, COOR)
    return row, column

def validate_coor(message, COOR):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input in COOR:
                valid = True
            else:
                print('\nEnter a valid coordinate number.')
        except ValueError:
            print('\nEnter a valid integer.')
    return user_input

def check_coors(user_coor_1, user_coor_2, board, asterisks_board, N):
    if user_coor_1 == user_coor_2:
        N -= 1
        print(f'\nThose are the same coordinates...no. You have {N} chances left.')    
    elif board[user_coor_1[0]][user_coor_1[1]] == board[user_coor_2[0]][user_coor_2[1]]:
        asterisks_board[user_coor_1[0]][user_coor_1[1]] = board[user_coor_1[0]][user_coor_1[1]]
        asterisks_board[user_coor_2[0]][user_coor_2[1]] = board[user_coor_2[0]][user_coor_2[1]]
    else:
        N -= 1
        print(f'\nNot a match. You have {N} chances left.')
    return asterisks_board, N

def win_lose_check(board, asterisks_board, N):
    if board == asterisks_board:
        print('You win')
        exit()
    elif N == 0:
        print('You lose\n')
        pprint(board)    
        exit()
    else:
        pass

def main():
    print('Welcome to the Memory Game')
    print('You have 10 chances to find all of the letter pairs.')
    print('You must input the coordinates from 0 to 3 for the position on the 4x4 board.\n')
    board = create_board()
    asterisks_board = create_asterisks_board(board)
    game_on(board, asterisks_board)
    
if __name__ == '__main__':
    main()
