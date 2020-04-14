"""The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . ."""

num = eval(input("How many Fibonacci Numbers do you want to Print: "))
first_number = 0
second_number = 1
print(first_number)
print(second_number)
for i in range(2,num):

    next_number =first_number + second_number
    first_number = second_number
    second_number = next_number

    print(next_number)






