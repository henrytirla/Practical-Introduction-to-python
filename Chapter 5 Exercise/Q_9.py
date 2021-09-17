from math import sqrt
count = 0
for num in range(1, 1001):
    if sqrt(num) % 1 != 0 and (num**(1/3)) % 1 != 0 and (num**(1/5)) % 1 != 0:
        count+=1
print(f'There are {count} numbers that are not perfect squares, cubes, or fifths.')
