# Magic Square

import numpy as np

array = np.random.randint(1, 5, size = (4, 4))
row_sum = array.sum(axis = 1)
column_sum = array.sum(axis = 0)
print(array)
print('')
print(row_sum)
print(column_sum)
