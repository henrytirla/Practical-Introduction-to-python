"""Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm """


hour = eval(input("Enter Hour Between 1 and 12: "))

enter_am_pm = input("Choose 1 for AM and 2 for pm")

future_hour = eval(input("Enter Hours in the future: "))

if enter_am_pm == 1:
    print("Future Hours ", enter_am_pm + future_hour)



