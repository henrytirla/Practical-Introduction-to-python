"""Write a program in which you have a list that contains seven integers that can be 0 or 1. Find
the first nonzero entry in the list and change it to a 1. If there are no nonzero entries, print a
message saying so."""

from random import randint

L = [randint(0, 1) for i in range(7)]
print('The initial list is the following: ')
print(L)
print('')
valid = False
while not valid:
    try:
         i = L.index(0)
         print(f'The first zero occurs at index {i}.')
         print('\nThe new list is the following: ')
         L[i] = 1
         print(L)
         valid = True
    except ValueError:
        print('There are no zero entries.')
        break
