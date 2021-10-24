"""Write a program that generates a random number between 1 and 10 and prints your name
that many times."""

from random import randint
x=input("Enter your Name:")
n = randint(1,10)
for i in range(n):
    print(x)
