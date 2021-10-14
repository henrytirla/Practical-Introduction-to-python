"""
A 4000-year old method to compute the square root of 5 is as follows: Start with an initial
guess, say 1. Then compute
((1 + (5/1)) / 2) = 3.
Next, take that 3 and replace the 1’s in the previous formula with 3’s . This gives
((3 + (5/3)) / 2) = 7/3 ≈ 2.33.
Next replace the 3 in the previous formula with 7/3. This gives
((7/3) + (5/(7/3)))/2 = 47/21 ≈ 2.24.

If you keep doing this process of computing the formula, getting a result, and plugging it back
in, the values will eventually get closer and closer to sqrt(5). This method works for numbers
other than 5. Write a program that asks the user for a number and uses this method to estimate
the square root of the number correct to within 10**−10. The estimate will be correct to within
10**−10 when the absolute value of the difference between consecutive values is less than 10**−10.
"""

def validate_input(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nPlease enter a positive number.')
        except:
            print('\nSorry, an integer was not inputted. Please enter an integer.')
    return user_input

def limit_squ_rt(valid_num):
    x = 1
    root = 10
    while True:
        root = round((x + (valid_num / x)) / 2, 10)
        if abs(x - root) < 10**-10:
            return root
        x = root

def main():
    message = 'Enter a number to find the limit of the square root: '
    valid_num = validate_input(message)
    squ_rt = limit_squ_rt(valid_num)
    print(f'\nThe limit of square root of {valid_num} is {squ_rt}.')

if __name__ == '__main__':
    main()
