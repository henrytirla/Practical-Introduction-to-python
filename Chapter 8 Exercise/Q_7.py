"""
Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs.
"""

from enum import Enum
from random import sample

class lottery(Enum):
    LOTTERY_NUM = [i for i in range(1,11)]

ITERATIONS = 1000

def lottery_hand():
    # Used sample function instead of calling the num of draws globally to practice with it.
    L = sample(lottery.LOTTERY_NUM.value, 6)
    return L

def winning_hand(ITERATIONS):
    count = 0
    for i in range(ITERATIONS):
        user_hand = lottery_hand()
        comp_hand = lottery_hand()
        if user_hand == comp_hand:
            count += 1
    return count      
    
def main():
    won = winning_hand(ITERATIONS)
    print((won/ITERATIONS) * 100)

if __name__ == '__main__':
    main()
