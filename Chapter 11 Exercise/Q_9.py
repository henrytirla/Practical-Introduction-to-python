"""
Using the card dictionary from earlier in the chapter, deal out three cards. Determine the
following:
(a) If the three cards form a flush (all of the same suit)
(b) If there is a three-of-a-kind (all of the same value)
(c) If there is a pair, but not three-of-a-kind
(d) If the three cards form a straight (all in a row, like (2, 3, 4) or (10, Jack, Queen))
"""

from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def get_cards():
    rand_cards = sample(Cards.DECK.value, 3)
    return rand_cards

def flush(hand):
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']:
        print('\nYou have a flush.')
    else:
        print('\nYou don\'t have a flush.')

def three_of_a_kind(hand):
    if hand[0]['value'] == hand[1]['value'] == hand[2]['value']:
        print('\nYou have a three-of-a-kind.')
    else:
        print('\nYou don\'t have a three-of-a-kind.')

def pair(hand):
    try:
        for i in range(3):
            if hand[i]['value'] == hand[i+1]['value']:
                print('\nYou have a pair.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a pair.')

def straight(hand):
    face_val = []
    for i in range(3):
        face_val.append(hand[i]['value'])
    face_val.sort(reverse = True)
    try:
        for i in range(3):
            if (face_val[i] - face_val[i+1] == 1) and (face_val[i+1] - face_val[i+2] == 1):
                print('\nYou have a straight.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a straight.')

def main():
    hand = get_cards()
    print('The following below is your hand.\n')
    print(hand)
    flush(hand)
    three_of_a_kind(hand)
    pair(hand)
    straight(hand)
    
if __name__ == '__main__':
    main()
