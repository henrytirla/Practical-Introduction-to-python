""" Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51."""
# from random import randint
# for n in range(2,52):
#      x=randint(1,n)
#      print(x)

def factorial(num):
     if num == 1:
          return 1
     return num * factorial(num-1)

print(factorial(4))