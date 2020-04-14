"""Write a program that asks the user for a number and prints out the factorial of that number."""




number=eval(input("Enter a number: "))
factorial =1


if number == 0:
    print("Factorial of this number does not exist")

elif number ==1:
    print("Factorial of 0 is 1")

else:

 for number in range(1,number+1):
    factorial =  factorial * number


print(factorial)
    
