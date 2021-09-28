""" Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'."""

user_input = input("Enter 5 numbers :") #1 2 3 4 5

sepr = user_input.replace(" ", "+")

print(sepr)