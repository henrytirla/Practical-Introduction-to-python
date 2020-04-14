"""(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power."""

exponent_number = eval(input("Enter the Value of the Exponent: "))

find_a = 2**exponent_number%10
print("The Last two digits of the " , find_a)



## (b) Solution of this problem is change the value of 10 above to 100

## (c) Solution Use and if \else  statement to solve the problem.