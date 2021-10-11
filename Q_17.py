from pprint import pprint
import numpy as np

array = np.random.randint(5, size=(4,4))
pprint(array)
ave = array.mean()
print(f'The average of the matrix is {ave}.')
