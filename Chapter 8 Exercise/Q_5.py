"""
Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.
"""

from sys import exit
from random import choices
from enum import Enum

class quotes(Enum):
    QUOTE_LIST = {1:'Good Morning', 2:'Good Afternoon', 3:"Good Evening"}

MENU_CHOICES = [1,2]

def validate_user_input(user_input):
    valid = False
    while not valid:
        valid_user_input = input(user_input)
        try:
            valid_user_input = int(valid_user_input)
            if valid_user_input in MENU_CHOICES:
                valid = True
            else:
                print('\nPlease enter a valid choice.')
        except ValueError:
            print(f'Sorry, "{valid_user_input}" is not a valid choice.')
    return valid_user_input

def exit_or_not(valid_menu_choice):
    if valid_menu_choice == 1:
        return
    else:
        exit()

def get_quote():
    q = choices(list(quotes.QUOTE_LIST.value.values()))
    return q
    
def main():
    print('Quote-of-the-Day')
    print('')
    print('Enter "1" to recieve the quote of the day.')
    print('Enter "2" to exit.')
    user_input = 'Please enter 1 or 2: '
    valid_menu_choice = validate_user_input(user_input)
    exit_or_not(valid_menu_choice)
    quote = get_quote()
    print(quote)

if __name__ == '__main__':
    main()
