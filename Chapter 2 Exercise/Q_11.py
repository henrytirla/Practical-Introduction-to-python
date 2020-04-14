"""Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be."""
n=eval(input("Enter a number to specify how high you want your box: "))
for rows in range(n):
    for column in range(n):
        if (rows == 0 or rows == n-1 or column == 0 or column == n-1):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()