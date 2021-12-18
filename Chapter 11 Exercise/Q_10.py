"""
Using the card dictionary from earlier in the chapter run a Monte Carlo simulation to estimate
the probability of being dealt a flush in a five card hand. See Exercise 32 of Chapter 10 for
more about Monte Carlo simulations.
"""

# Note, chances to get a flush in 5-card is about 1 out of 509 hands.

from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def validate_num(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nEnter a huge number for how many hands to play.')
        except ValueError:
            print('\nEnter a valid integer.')
    return user_input

def flush(COUNT, num):
    for i in range(num):
        hand = get_cards()
        if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
            COUNT += 1
        else:
            pass
    return COUNT

def get_cards():
    rand_cards = sample(Cards.DECK.value, 5)
    return rand_cards

def main():
    COUNT = 0
    message = 'Enter the number of hands to play: '
    num = validate_num(message)
    prob = flush(COUNT, num)
    print(f'\n{prob} hand(s) had a flush.\n')
    print(f'The probability to get a flush from {num} hands is {round((prob/num)*100, 3)}%.')

if __name__ == '__main__':
    main()
