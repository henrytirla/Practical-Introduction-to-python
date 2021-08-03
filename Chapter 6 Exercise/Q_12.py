"""Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS."""


user_input = input("Enter word: ")
result = ""
for letters in range(len(user_input)):
    if letters % 2 != 0:
       result =  result + user_input[letters].upper()
    else:
        result = result + user_input[letters].lower()

print(result)

