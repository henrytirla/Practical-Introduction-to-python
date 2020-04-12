"""Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

*
***
*****
*******
*****
***
* """


# n=eval(input("Enter a number to specify how high you want your triangle: "))
n=17
for rows in range (n):
    for columns in range(0,n-rows-1):
      print(end="")
    for columns in range(0,rows+1):
        print("*", end="")

    print()

