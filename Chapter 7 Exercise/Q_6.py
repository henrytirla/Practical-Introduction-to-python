# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.

import random
import math
number_list = []
square_list =[]
alpha_list =[]

for i in range(0,49):
    number_list.append(i)
print(number_list)

for j in range(0,number_list[i]):
    square_list.append(j*j)

print(square_list)

alphabet=['','a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t']

for alpha in range(1,len(alphabet)):
     alpha_list.append(alphabet[alpha]*alpha)
print(alpha_list)



