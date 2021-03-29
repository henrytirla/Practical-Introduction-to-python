"""Modify the higher/lower program so that when there is only one guess left, it says 1 guess,
not 1 guesses."""

from random import randint
secret_num = randint(1,100)
num_guesses = 0
guess = 0
while guess != secret_num and num_guesses <= 4:
           guess = eval(input('Enter your guess (1-100): '))
           num_guesses  += 1
           if 5-num_guesses == 1 and guess > secret_num:
               print("LOWER.", 5 - num_guesses, "GUESS left")
           elif 5 - num_guesses == 1 and guess < secret_num:
                   print("Higher.", 5 - num_guesses, "GUESS left")
           elif guess < secret_num and 5-num_guesses !=1:
               print("HIGHER.", 5-num_guesses, "guesses left")
           elif guess > secret_num and 5-num_guesses !=1:
              print("LOWER.", 5-num_guesses, "guesses left")

           else:
              print('You got it!')
           if num_guesses==5 and guess != secret_num:
              print('You lose. The correct number is', secret_num)