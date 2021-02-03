"""Write a program to help with word games. The user enters a word and the program uses the
wordlist to determine if the user’s word is a real word or not."""

file1 = open("wordlist.txt","r")
str_data =[line.strip('\n') for line in file1]
user_input = input("Enter a Word:")

for words in str_data:
    if user_input == words:
        #print("User word is real")
        pass

