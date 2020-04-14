"""Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]"""

seconds= eval(input("Enter the number of seconds: "))


time_in_minutes =int(seconds /60)
time_in_seconds = seconds % 60

print("The  time is " , time_in_minutes,"minutes ", time_in_seconds,"seconds")
