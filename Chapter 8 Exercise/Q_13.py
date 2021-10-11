L = ['apple', 'car', 'tree', 'I', 'watch', 'internet']
print(L)
M = [s[1:] for s in L]
print(M)
N = [len(s) for s in L]
print(N)
O = [s for s in L if len(s) >= 3]
print(O)
