'''
Write a class called Poker_hand that has a field that is a list of Card objects. There should be
the following self-explanatory methods: has_royal_flush, has_straight_flush, has_four_of_a_kind,
has_full_house, has_flush, has_straight, has_three_of_a_kind, has_two_pair, has_pair.
There should also be a method called best that returns a string indicating what the best hand
is that can be made from those cards.
'''

import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        names = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            return '{} of {}'.format(self.value, self.suit)
        else:
            return '{} of {}'.format(names[self.value - 11], self.suit)


class PokerHand:
    def __init__(self):
        self.deck = [{'value': i, 'suit': c}for c in ['spades', 'clubs',
                                                      'hearts', 'diamonds']for i in range(2, 15)]
        self.deals = random.sample(self.deck, 5)
        self.suits = [(self.deals[i])['suit'] for i in range(len(self.deals))]
        self.values = [((self.deals[i])['value'])
                       for i in range(len(self.deals))]

        self.cards = [Card(self.values[i], self.suits[i]).__str__()
                      for i in range(len(self.deals))]
        self.values.sort()

        self.deck_count = {i: self.values.count(i) for i in self.values}
        self.card_count = [self.deck_count[i] for i in self.deck_count]
        self.card_count.sort()

    def straigth(self):

        return self.values == [self.values[0]+i for i in range(5)] or self.values == [2, 3, 4, 5, 14]

    def flush(self):
        return self.suits.count(self.suits[0]) == 5

    def straigth_flush(self):
        return self.straigth() and self.flush()

    def four_of_a_kind(self):
        return self.card_count == [1, 4]

    def three_of_a_kind(self):
        return self.card_count == [1, 1, 3]

    def two_pairs(self):
        return self.card_count == [1, 2, 2]

    def full_house(self):
        return self.card_count == [2, 3]

    def royal_flush(self):
        return self.values == [10, 11, 12, 13, 14] and self.flush()

    def one_pair(self):
        return self.card_count == [1, 1, 1, 2]

    def best_hand(self):
        for i, card in enumerate(self.cards):
            print(f'card {i+1}.', card)

        if self.royal_flush():

            return ("BEST HAND IS ROYAL FLUSH  ")

        elif self.straigth_flush():
            return("BEST HAND IS STRAIGHT FLUSH")

        elif self.four_of_a_kind():
            return("BEST HAND IS FOUR OF A KIND ")

        elif self.full_house():
            return("BEST HAND IS  FULL HOUSE")

        elif self.flush():
            return("BEST HAND IS FLUSH ")

        elif self.straigth():
            return("BEST HAND IS STRAIGHT ")

        elif self.three_of_a_kind():
            return("BEST HAND IS THREE OF A KIND")

        elif self.two_pairs():
            return("BEST HAND IS TWO PAIRS")

        elif self.one_pair():
            return("BEST HAND IS ONE PAIR")
        else:
            return "YOU HAVE HIGH CARDS"
          
poker = PokerHand()
print(poker.best_hand())
