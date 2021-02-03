"""Suppose we write all the words in the wordlist backwards and then arrange these backwards
words alphabetically. Write a program that prints the last word in this modified wordlist."""


file1 = open("wordlist.txt","r")
str_data = [line.strip('\n') for line in file1]

for words in str_data:
    rev =reversed(words)
print(list(rev))

