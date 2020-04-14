""""18. Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]"""

##To fully understand this problem you have to understand what are the differences between quaters ,dimes ,nickels and pennies.
import sys

""" Quater = 25cents
    Dimes = 10cents
    Nickel = 5cents
    Penny = 1cent
    
"""


number = eval(input("Enter a number beween 0-99: "))
if number < 0 or number > 99:
    print("You entered a number in the wrong range!!!!!")
    sys.exit()

else:
      Quater = number // 25
      Dimes = number // 10
      Nickel = number // 5
      Penny = number // 1

print("Quater = ",Quater, "Dimes = ", Dimes, "Nickel = ", Nickel, "Penny = ", Penny)