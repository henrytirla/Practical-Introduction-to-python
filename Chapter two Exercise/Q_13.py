"""Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be."""
n=eval(input("Enter a number to specify how high you want your triangle: "))

for rows in range (n,0,-1):
    for colums in range(rows):
        print("*", end=" ")

    print()



