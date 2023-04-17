"""

The goal of this exercise is to see if you can mimic the behavior of the in operator and the
count and index methods using only variables, for loops, and if statements.

(a) Without using the in operator, write a program that asks the user for a string and a letter
and prints out whether or not the letter appears in the string.

(b) Without using the count method, write a program that asks the user for a string and a
letter and counts how many occurrences there are of the letter in the string.

(c) Without using the index method, write a program that asks the user for a string and
a letter and prints out the index of the first occurrence of the letter in the string. If the
letter is not in the string, the program should say so
"""


#a
# string = input("Enter String: ")
# letter = input("Enter Letter: ")
# index =0
# found= False
#
#
# while index < len(string):
#     if string[index] == letter:
#         found= True
#         #print("Letter Found")
#         break
#     else:
#         index+=1







#b

string = input("Enter String: ")
letter = input("Enter Letter: ")
index =0
found= False
count= 0


while index < len(string):

    if string[index] == letter:
        index+=1
        count +=1


    else:
        index += 1
print(f"Number occures {count} number of times")

#c edit solution a to have answer to c