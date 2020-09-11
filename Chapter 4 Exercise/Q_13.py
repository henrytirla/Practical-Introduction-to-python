"""Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie."""

from random import  randint
game = 0

rock = 1
paper =2
scissors =3
wins =0
loose =0


for game in range(5):
    print("Game",game,"Start")

    my_hand = eval(input("Choose Rock , paper or scissors: "))
    computer_hand = randint(1, 3)
    if my_hand == computer_hand :
        print ("You and Computer Played the same hand its a tie..")
    elif my_hand == rock and computer_hand == scissors:
        print("Yay I crushed the computer scissors")
        wins += 1
    elif my_hand == rock and computer_hand == paper:
        print("Oops Computer Cover my Rock")
        loose += 1
    elif my_hand == paper and computer_hand == rock:
        print("Yay!! I covered computer rock haha")
        wins += 1
    elif  my_hand == paper and computer_hand == scissors:
        print("Oops Computer cut me up into piece")
        loose += 1
    elif my_hand == scissors and computer_hand == rock:
        print("Oops Computer Shattered My scissors")
        loose += 1
    elif my_hand == scissors and computer_hand == paper:
        print("Yay I cut up computer paper into pieces")
        wins += 1

if wins > loose:
    print("You win ", "You Scored ",wins,"Computer Scored",loose)

else:
    print("You loosed Try Again")

