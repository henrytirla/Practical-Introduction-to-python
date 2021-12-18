"""Write a simple lottery drawing program. The lottery drawing should consist of
six different
numbers between 1 and 48."""
import random
from random import randint
lottery_num = []


while len(lottery_num) < 6:

    random_num = random.randint(1,48)
    lottery_num.append(random_num)

print(lottery_num)




