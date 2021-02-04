"""Crossword cheater: When working on a crossword puzzle, often you will have a word where
you know several of the letters, but not all of them. You can write a computer program to
help you. For the program, the user should be able to input a word with the letters they
know filled in and asterisks for those they don’t know. The program should print out a list
of all words that fit that description. For example, the input th***ly should return all the
words that could work, namely thickly and thirdly."""

file1 = open("wordlist.txt","r")
str_data =[line.strip("\n") for line in  file1]
user_input = input("Enter Word You Know: ")

for words in str_data:
    if user_input[:2] == words[:2] and user_input[-2:] == words[-2:] and len(user_input) == len(words):
        for i in user_input:
            if i in words:
                print(words)