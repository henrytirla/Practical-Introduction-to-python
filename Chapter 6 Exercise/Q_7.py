"""Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards."""

user_word = input("Enter a Word: ")
#eg kayak

if user_word == user_word[::-1]:
    print(user_word," Yay this is a palindrome")

else:
    print(user_word ," Sorry this is not a Palindrome")

