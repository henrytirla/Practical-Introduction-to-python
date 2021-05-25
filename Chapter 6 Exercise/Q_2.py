""""A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string."""


word = input("Enter a text: ")
print("Number of words in text is: ",word.count(' ') + 1)
