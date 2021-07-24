"""Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH
EE
YY"""

user_string = input("Enter String: ")

for letter in user_string:
    print(letter * 2)