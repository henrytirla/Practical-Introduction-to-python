"""" A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year. """


year = eval(input("Enter a Year: "))
#
# if year < 2000:
#     print("Enter any year as from 2000")

for years in range(1600,year):
    if years % 4 == 0 or years % 100 == 0 and years % 400 == 0:
        print( years)
