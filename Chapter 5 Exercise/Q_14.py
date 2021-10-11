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
