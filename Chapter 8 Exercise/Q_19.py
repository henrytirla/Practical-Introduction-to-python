print('\nProblem 19\n')
from pprint import pprint
from itertools import cycle

iterator = cycle(range(2))
L = [[next(iterator) for column in range(8)] for row in range(8)]
pprint(L)

print('\nProblem 19 - Alternate Solution\n')
from pprint import pprint

def alternate():
    while True:
        yield 1
        yield 0

alternator = alternate()
L = [[next(alternator) for column in range(8)] for row in range(8)]
pprint(L)
