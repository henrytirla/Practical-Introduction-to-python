"""A good program will make sure that the data its users enter is valid. Write a program that
asks the user for a weight and converts it from kilograms to pounds. Whenever the user
enters a weight below 0, the program should tell them that their entry is invalid and then ask
them again to enter a weight.

[Hint: Use a while loop, not an if statement].

"""


while True:
    weight =eval(input("Enter Weight in Kg: "))
    if weight < 0:
        print("Illegal weight entered")
    else:
        pounds = weight * 2.2
        print("Your weight in Pounds is",pounds)