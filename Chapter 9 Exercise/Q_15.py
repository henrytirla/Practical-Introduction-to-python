"""
Write a program to play the following game. There is a list of several country names and the
program randomly picks one. The player then has to guess letters in the word one at a time.
Before each guess the country name is displayed with correctly guessed letters filled in and
the rest of the letters represented with dashes. For instance, if the country is Canada and the
player has correctly guessed a, d, and n, the program would display -ana-da. The program
should continue until the player either guesses all of the letters of the word or gets five letters
wrong.
"""

from random import choice
from string import ascii_lowercase
from re import finditer
from sys import exit

COUNTRY_LIST = ['canada', 'england', 'japan', 'china', 'germany', 'scotland', 
                'chad', 'ghana', 'mexico', 'ireland', 'korea', 'denmark']

def game_on():
    num_guesses = 5
    country = get_country(COUNTRY_LIST)
    country_placeholder = country
    for i in country:
        country = country.replace(i, '*')
    while num_guesses > 0:
        print(country)
        message = 'Enter a letter to guess: '
        guess = validate_letter(message)
        if guess in country_placeholder:
            valid_letter = [x.start() for x in finditer(guess, country_placeholder)]
            for j in valid_letter:
                country = country[:j] + country[j].replace('*', guess) + country[j+1:]
        else:
            num_guesses -= 1
            print(f'No "{guess}" in the country\'s name. You have {num_guesses} number of guesses left.\n')
        win_lose(num_guesses, country, country_placeholder)
        
def get_country(COUNTRY_LIST):
    rand_country = choice(COUNTRY_LIST)
    return rand_country

def validate_letter(message):
    valid = False
    while not valid:
        try:
            user_input = input(message)
            if (user_input in ascii_lowercase) and (len(user_input) == 1):
                valid = True
            else:
                print('\nPlease enter a valid letter as a guess: ')
        except:
            pass
    return user_input

def win_lose(num_guesses, country, country_placeholder):
    if num_guesses == 0:
        print(f'You ran out of guesses. The country is {country_placeholder.capitalize()}. You lose.')
    elif country == country_placeholder:
        print(f'\nYes the country was {country.capitalize()}.')
        print('You Win!')
        exit()
    else:
        pass

def main():
    print('Welcome to the Country Guessing Game')
    print('You have 5 guesses.\n')
    game_on()

if __name__ == '__main__':
    main()
