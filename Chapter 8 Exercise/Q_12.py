def validate_input(message):
    valid = False
    while not valid:
        user_input = input(message)
        num = user_input.split('-')
        try:
            if (len(num[0]) == 1) and (len(num[1]) == 3) and (len(num[2]) == 3) and (len(num[3]) == 4):
                valid = True
            elif (len(num[0]) == 3) and (len(num[1]) == 3) and (len(num[2]) == 4):
                valid = True
            else:
                print('Your format is off. Please enter a valid phone number.')
        except IndexError:
            print('A phone number was not inputted.')
    return user_input

def main():
    print('Welcome to Phone Number Validation.\n')
    print('The phone number format is 1-ABC-DEF-GHIJ or ABC-DEF-GHIJ.')
    message = 'Enter a valid phone number: '
    valid_num = validate_input(message)
    print(f'\nThe number, {valid_num}, is valid.')

if __name__ == '__main__':
    main()
