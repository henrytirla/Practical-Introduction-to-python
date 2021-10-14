"""
Write a program to play the following simple game. The player starts with $100. On each
turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
correct guess and loses $10 for each incorrect guess. The game ends either when the player
runs out of money or gets to $200.
"""

from enum import Enum
from random import choice

class coin(Enum):
    FACE = {'h':'Heads', 't':'Tails'}

MONEY = 100

def heads_tails(MONEY):
    while 0 < MONEY < 200:
        rand_face = coin_face()
        message = 'Enter "h" for heads or "t" for tails: '
        user_guess = validate_input(message)
        print(rand_face)
        if rand_face == user_guess:
            MONEY += 9
            print(f'You guessed right! You now have ${MONEY}.')
        else:
            MONEY -= 10
            print(f'You guessed wrong! You now have ${MONEY}.')
    if MONEY < 0:
        print('You do not have any more money to play.')
    else:
        print(f'You have ${MONEY}. Good job. Good-bye.')
    
def coin_face():
    rand_face = choice(list(coin.FACE.value.keys()))
    return rand_face
    
def validate_input(message):
    valid = False
    while not valid:
        try:
            user_input = input(message)
            user_input = user_input.lower()
            if (user_input == 'h') or (user_input == 't'):
                valid = True
            else:
                print('\nPlease enter "h" or "t".')
        except:
            pass
    return user_input

def main():
    print('Welcome to Heads and Tails.')
    print('')
    print(f'You have ${MONEY} to start with.')
    print('')
    print('If you guess right, you get $9. If you guess wrong, you lose $10.')
    heads_tails(MONEY)
    
if __name__ == '__main__':
    main()
