"""Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

*
***
*****
*******
*****
***
* """

n = eval(input("Enter a number to specify how high you want your triangle: "))
for i in range(n):
    print(" "*(n-i)+" *"*(i+1))

for j in range(n-1):
    print(" "*(j+2)+" *"*(n-1-j))
    



