# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random
random_list = []
c=0
max_count=0
for i in range(100):
   n = random.randint(0,1)
   random_list.append(n)
print(random_list)


for j in random_list:
    c = c+1 if j == 0 else 0
    max_count = max(max_count,c)
print(max_count)
