"""Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe."""

first_string = input("Enter First String: ")
second_string = input("Enter Second String: ")


res = ""
if len(first_string) != len(second_string):
    print("Both Strings Do not have the same length")
    exit()
else:
    for i in range(len(first_string)):
         res =  res + first_string[i] + second_string[i]

    print(res)
