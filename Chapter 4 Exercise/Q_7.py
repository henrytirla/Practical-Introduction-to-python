"""Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise."""

num1 = eval(input("Enter First Number: "))
num2 = eval(input("Enter Second Number:"))

if num1 + 0.001 == num2:

     print("close")

elif num2 + 0.001 == num1:

     print("close")

else:
     print("Not close")
