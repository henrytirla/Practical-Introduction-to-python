"""Recall that, given a string s, s.index('x') returns the index of the first x in s and an error
if there is no x.
(a) Write a program that asks the user for a string and a letter. Using a while loop, the
program should print the index of the first occurrence of that letter and a message if the
string does not contain the letter.
(b) Write the above program using a for/break loop instead of a while loop."""

#a
def Firstletter():
    user_input =input("Input Word: ")
    letter = input("Choose Letter: ")
    count =0
    while  count <1:
        count+=1
        if letter in user_input:
           print(user_input.index(letter))
        else:
            print("Letter not found in word")



#Firstletter()

#b
def Firstletter2():
    user_input =input("Input Word: ")
    letter = input("Choose Letter: ")

    for character in user_input:
        if character == letter:
           print(user_input.index(character))

           break



Firstletter2()