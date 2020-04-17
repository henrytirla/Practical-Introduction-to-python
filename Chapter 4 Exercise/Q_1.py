"""Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch."""

import sys
length_cm = eval(input("Enter Lenth in Centimeters: "))
if length_cm < 0:
    print("You Have Entered an Invalid Number")
    sys.exit()

else:
    length_inches = length_cm / 2.54
    print(length_inches," inches")