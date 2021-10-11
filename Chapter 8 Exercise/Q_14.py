L = [num for num in range(100, 1001)]
M = []
count = 0
for i in L:
    i = str(i)
    if i == i[::-1]:
        count+=1
        M.append(int(i))
print(f'\nThere are {count} numbers that are a palindromic.\n')
print(M)
