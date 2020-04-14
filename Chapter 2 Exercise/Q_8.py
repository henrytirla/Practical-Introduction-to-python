"""Write a program that asks the user for their name and how many times to print it. The program
should print out the user’s name the specified number of times."""

ask_user = input("Please Enter Your Name: ")
printing_times = eval(input("How many times do you want to print your "))

for i in range(printing_times):
    print(ask_user)