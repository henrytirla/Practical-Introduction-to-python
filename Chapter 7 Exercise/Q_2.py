# Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.
import random
from random import randint

number_list =[]
count =0

for i in range(20):
    number_list.append(randint(1,100))

print(number_list)
number_list.sort()
print(number_list)
average = sum(number_list)/len(number_list)
print("Average of list",average)
print("Maximum Number",max(number_list))
print("Second Maximum Number",number_list[-2])
print("Minimum Number",min(number_list))
print("Second Minimum Number",number_list[1])

for i in number_list:
    if i%2==0:
     count += 1
print("Number of even Numbers in List",count)


