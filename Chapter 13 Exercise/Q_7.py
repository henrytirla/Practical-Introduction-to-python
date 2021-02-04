"""Write a function that takes an integer n and returns a random integer with exactly n digits. For
instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
that is really 93, which is a two-digit number."""

import random

def generate_num(n):

    random_num =random.randint(10 ** (n - 1), 10 ** n - 1)
    if random_num >100:
        print("Valid",random_num)
    else:
        print("invalid",random_num)



generate_num(3)