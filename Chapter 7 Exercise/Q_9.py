# When playing games where you have to roll two dice, it is nice to know the odds of each
# roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
# 17%. You can compute these mathematically, but if you don’t know the math, you can write
# a program to do it. To do this, your program should simulate rolling two dice about 10,000
# times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12.


from random import randint
dice_roll=[]
outcome ={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
sim =10000

for simulations in range(sim):
    first_dice_roll = randint(1,6)
    second_dice_roll = randint(1,6)

    sum_dice =(first_dice_roll + second_dice_roll)
    # print(sum_dice)
    outcome[sum_dice] += 1



for key in outcome.keys():
    # print("Percentage for rolling a sum of %s is:"%(key,outcome[key]/sim*100))
    print("Percentage for rolling a sum of %s is: %s" % (key, outcome[key] / sim * 100))

