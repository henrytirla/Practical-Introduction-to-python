""""Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.

An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
"""

hour = eval(input("Enter the the  Current Hour between 1-12 : "))
projected_hour = eval(input("Enter Projected Hour: "))

current_hour = hour + projected_hour

if current_hour > 12:
    current_hour = current_hour % 12


print("New Hour :",current_hour," O'clock")
