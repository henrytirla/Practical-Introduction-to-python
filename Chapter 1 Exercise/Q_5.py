"""Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below."""

num = eval(input("Enter a Number: "))

print("The square of",num,"is",num*num,".",sep=" ")
