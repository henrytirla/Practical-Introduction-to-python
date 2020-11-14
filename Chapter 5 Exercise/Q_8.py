"""Write a program that swaps the values of three variables a, b, and c, so that a gets the value
of b, b gets the value of c, and c gets the value of a."""


def swapThree(a, b, c):
    # Store sum of all in a
    a = a + b + c  # (a = 6)

    # After this, b has value of a
    b = a - (b + c)  # (b = 6 – (3+2) =1)

    # After this, c has value of b
    c = a - (b + c)  # (c = 6 – (1 + 3) = 2)

    # After this, a has value of c
    a = a - (b + c)

    return ("After swapping a =", a, ", b =", b, ", c =", c)


print(swapThree(1,2,3))

##credit https://www.geeksforgeeks.org/swap-three-variables-without-using-temporary-variable/