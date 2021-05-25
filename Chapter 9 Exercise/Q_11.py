"""Write a program that starts with an 5 X 5 list of zeroes and randomly changes exactly ten of
those zeroes to ones."""
from random import randint
list_50 =[0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0,]
i=0
total_zeros = len(list_50)
while (i <1):
    value = randint(0, total_zeros-1)
    list_50[value] = 1
    i = i+1
print(list_50)





