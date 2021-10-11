from string import ascii_letters, punctuation, digits
from random import sample, shuffle
from pprint import pprint
import numpy as np

# From string module, imported all corresponding characters and grouped them together in source variable.
source = ascii_letters + punctuation + digits

# Using sample function from random module, grabbed 18 random characters from source string.
# After which, the random chars cloned to create pairs for memory game. 
# Note, sample returns a list.
chars = sample(source, 18) * 2

# Used shuffle function to randomize the list of characters
shuffle(chars)

# Used numpy instead of list comprehensions to create an array of the chars at a 6x6 size.
# After which, the array was converted to a list using the .tolist() method.
L = np.array(chars).reshape(6,6).tolist()
pprint(L)
