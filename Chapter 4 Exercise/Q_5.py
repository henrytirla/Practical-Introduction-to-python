"""Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not."""

### This isn't the exact answer to this but it was fun to let the user guess again and again.
from random import randint

random_number = randint(1,10)


game = 0
while game < 6:
 guess = eval(input("Guess generated random number: "))
 game =game + 1


 if guess == random_number:
    print("You Guessed right!")
    break
 elif guess > random_number:
    print("Input number is greater than Random number")

 elif guess < random_number:
    print("Input is less than random number")



