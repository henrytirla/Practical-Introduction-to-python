"""
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.
"""

from random import randint

score = 0

for i in range(5):
  comp_guess = randint(1, 10)
  user_guess = eval(input('Enter guess between 1 and 10: '))
  while user_guess < 0 or user_guess > 10:
    user_guess = eval(input('Invalid. Enter guess between 1 and 10: '))
    continue
  if user_guess == comp_guess:
    score += 10
    print(f'You guessed right! Your score is {score}.')
  else:
    score -= 1
    print(f'Wrong. Computer guessed {comp_guess}. You guessed {user_guess}.')
print(f'\nAfter 5 rounds, your total score is {score}.')
