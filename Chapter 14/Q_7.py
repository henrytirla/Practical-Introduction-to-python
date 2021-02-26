"""Use the Standard_deck class of this section to create a simplified version of
the game War.
In this game, there are two players.
Each starts with half of a deck. The players each deal
the top card from their decks and
whoever has the higher card wins the other player’s cards
and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from
play (this differs from the actual game, but is simpler to program). The game ends when one
player runs out of cards."""

from random import randint


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


import random


class Card_group:
    def __init__(self, cards=[]):
        self.cards = cards

    def nextCard(self):
        return self.cards.pop(0)

    def hasCard(self):
        return len(self.cards) > 0

    def size(self):
        return len(self.cards)

    def shuffleCard(self):
        return random.shuffle(self.cards)


class Standard_deck(Card_group):
    def __init__(self):
        self.cards = []
        for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for v in range(2, 15):
                self.cards.append(Card(v, s))  # hỏi chỗ này


class War(Standard_deck):
    def __init__(self):
        Standard_deck.__init__(self)
        self.shuffleCard()
        self.player1 = []
        self.player2 = []
        self.__splitCardToPlayer()

    def __splitCardToPlayer(self):
        cardLength = len(self.cards)
        for i in range(0, cardLength, 2):
            self.player1.append(self.nextCard())
            self.player2.append(self.nextCard())



    def __popCard(self, playerNumber):
        if playerNumber == 1:
            return self.player1.pop()
        if playerNumber == 2:
            return self.player2.pop()

    def play(self):
        print('Playing card')
        while len(self.player1) > 0 and len(self.player2) > 0:
            card1 = self.__popCard(1)
            card2 = self.__popCard(2)
            if card1.value > card2.value:
                self.player1.append(card1)
            elif card2.value > card1.value:
                self.player2.append(card2)

        if len(self.player1) > 0:
            print("player 1 wins")
        elif len(self.player2) > 0:
            print("player 2 wins")
        else:
            print("noone win")


deck = War()
deck.play()

#reference https://github.com/monkeybuzinis/Python/blob/master/14.object-oriented/7.py