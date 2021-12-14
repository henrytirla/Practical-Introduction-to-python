"""
Randomly generate a 6 × 6 list that has exactly 12 ones placed in random locations in the list.
The rest of the entries should be zeroes.
"""

from pprint import pprint
from random import randint

L = [[0 for column in range(6)]for row in range (6)]
i = 0

# Must use a while loop instead of for loop because can not repeat iterations.
while i < 12:
    a, b = randint(0, 5), randint(0, 5)
    if L[a][b] == 1:
        pass
    else:
        L[a][b] = 1
        i += 1
pprint(L)
