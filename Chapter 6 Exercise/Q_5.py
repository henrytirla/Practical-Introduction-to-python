"""Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string. Typical output is shown below:

Enter your string: Qbert

Q*ert!!!"""

string = input("Enter a String: ")

new_string = string[0]+"*"+string [2:]

print(new_string + "!!!")
