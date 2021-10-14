"""
Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
"""

from enum import Enum
from time import sleep
from sys import exit
from random import choice

VALID_MENU_CHOICE = [1,2]

class lottery(Enum):
    LOTTERY_NUM = [i for i in range(1,49)]
    
def validate_user_input(message):
    valid = False
    while not valid:
        valid_input = input(message)
        try:
            valid_input = int(valid_input)
            if valid_input in VALID_MENU_CHOICE:
                valid = True
            else:
                print('\nPlease enter a valid choice.')
        except ValueError:
            print(f'Sorry, "{valid_input}" is not a valid choice.')
    return valid_input

def get_exit(valid_input):
    if valid_input == 2:
        exit()
    # If it does not exit, then it assumes to continue and will return to main().

def lottery_game(drawn_nums):
    print('\nThe following are the winning numbers: \n')
    for i in range(drawn_nums):
        win_num = choice(lottery.LOTTERY_NUM.value)
        print(win_num)
        sleep(3)

def main():
    print('Welcome to the Lottery!')
    print('')
    print('Record five numbers between 1 and 48 before starting.')
    print('')
    print('Enter "1" when you are ready to play.')
    print('Enter "2" to exit.')
    drawn_nums = 6 # Defines how many numbers will be drawn.
    message = 'Enter 1 or 2: '
    valid_user_choice = validate_user_input(message)
    get_exit(valid_user_choice)
    lottery_game(drawn_nums)
    print('\nThank you for playing the lottery!')

if __name__ == '__main__':
    main()
