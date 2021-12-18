"""
Write a program that checks to see if a 4 × 4 list is a magic square. In a magic square, every
row, column, and the two diagonals add up to the same value.
"""

import numpy as np

array = np.random.randint(1, 5, size = (4, 4))
row_sum = array.sum(axis = 1)
column_sum = array.sum(axis = 0)
print(array)
print('')
print(row_sum)
print(column_sum)

# I believe This is incorrect.
