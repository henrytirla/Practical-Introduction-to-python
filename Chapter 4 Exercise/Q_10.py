""""Write a multiplication game program for kids. The program should give the player ten randomly
generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is. """

from random import  randint


questions = 0

for questions in range(10):
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    questions += 1

    print("Question :",questions ,num_1 ,"X",num_2)
    solution =eval(input("Enter Solution: "))

    if(solution == num_1 * num_2):
      print("YaY you got it Right!!")

    else:
       print(solution,"Your Answer is Wrong")

