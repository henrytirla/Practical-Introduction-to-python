"""Print a box like the one below.
*******************
* *
* *
*******************"""


for rows in range(5):
    for columns in range(5):
        if (rows == 0 or rows == 5-1 or columns == 0 or columns == 5-1):
            print("*" , end="  ")

        else:
            print(" ", end="  ")

    print()