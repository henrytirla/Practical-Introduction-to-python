"""
This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. The host, Monty Hall, shows you three doors. 
Behind one of those doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who knows behind which door the prize lies, 
then opens up one of the doors that doesn’t contain the prize. There are now two doors left, and Monty gives you the opportunity to change your
choice. Should you keep the same door, change doors, or does it not matter?

Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you
would win by not switching.
"""

from random import randint, choice

count = 0

for i in range(1000):
  user_guess = randint(1, 3)
  prize = randint(1, 3)
  if prize == 1:
    doors = [1, randint(2,3)]
    if user_guess not in doors:
      user_guess = choice(doors)
      if user_guess == prize:
        count += 1
    else:
      if user_guess == prize:
        count += 1
  if prize == 2:
    doors = [2, randint(1,3)]
    if user_guess not in doors:
      user_guess = choice(doors)
      if user_guess == prize:
        count += 1
    else:
      if user_guess == prize:
        count += 1
  if prize == 3:
    doors = [3, randint(2,3)]
    if user_guess not in doors:
      user_guess = choice(doors)
      if user_guess == prize:
        count += 1
    else:
      if user_guess == prize:
        count += 1
percentage = round((count/1000) * 100, 2)
print(f'User chose the correct door {count} amount of times out of 1000. The percentage is {percentage}%.')
