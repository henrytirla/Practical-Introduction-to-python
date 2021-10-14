"""
The following is useful as part of a program to play Battleship. Suppose you have a 5 × 5 list
that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the
list at that row and column is a one, the program should print Hit and otherwise it should
print Miss.
"""

from random import randint
from pprint import pprint

MAP = [[randint(0,1) for column in range(5)] for row in range(5)]

def validate_input(row_input, column_input, flag):
    valid = False
    while not valid:
        try:
            if flag == 0:
                user_input = int(input(row_input))
            else:
                user_input = int(input(column_input))
            if 0 <= user_input <= 4:
                valid = True
            else:
                print('\nSorry you did not enter a number from the choices.')
        except ValueError:
            print('\nYou did not enter a number.')
    return user_input

def hit_miss(row, column):
    if MAP[row][column] == 1:
        print('Hit')
    else:
        print('Miss')         

def main():
    print('Welcome to Battleship.')
    print('')
    print('The board is 5x5 (25 choices total).')
    print('You will first inout row and then column to indicate the point you want to target.')
    print('The choices for the row and column will be 1 through 5.')
    row_input = 'Enter 0, 1, 2, 3, or 4 for row: '
    column_input = 'Enter 0, 1, 2, 3, or 4 for column: '
    flag = 0
    row = validate_input(row_input, column_input, flag)
    flag = 1
    column = validate_input(row_input, column_input, flag) 
    hit_miss(row, column)
    pprint(MAP)

if __name__ == '__main__':
    main()
