"""
Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the
following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column.
"""

import numpy as np
from pprint import pprint

array = np.random.randint(1, 101, size = (10, 10))
pprint(array)
print('')

# Grabbed 3rd row.
third_row_max = array[2].max(axis = 0) # axis = 0 is row
print(third_row_max)
print('')

# Grabbed 6th column.
column = array[:,5].reshape(1,-1)
sixth_column_min = column.min()
print(sixth_column_min)

print('\nProblem 19\n')
from pprint import pprint
from itertools import cycle
iterator = cycle(range(2))
L = [[next(iterator) for column in range(8)] for row in range(8)]
pprint(L)
