"""Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
1."""

count = 0


for i in range(1,100):
    if (i**i % 10 == 1 or i**i % 10 == 9):
        count += 1
        #print(i) can be use to confirm numbers displayed squares actually end with one
print(count)