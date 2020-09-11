"""Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9."""

count = 0


for i in range(1,100):
    if (i**i % 10 == 4 or i**i % 10 == 7 ):
        count += 1
        # print(i)
print(count)