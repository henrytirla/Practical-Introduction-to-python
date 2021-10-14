"""
Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
"""

L = ['apple', 'car', 'tree', 'I', 'watch', 'internet']
print(L)
M = [s[1:] for s in L]
print(M)
N = [len(s) for s in L]
print(N)
O = [s for s in L if len(s) >= 3]
print(O)
