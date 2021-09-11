
"""Write a program that asks the user to enter a word that contains the letter a. The program
should then print the following two lines: On the first line should be the part of the string up
to and including the the first a, and on the second line should be the rest of the string. Sample
output is shown below:

Enter a word: buffalo
buffa
lo"""

input_string = input("Enter a String that contains the letter a: ")
#
for letters in range(len(input_string)):

    if input_string[letters] == "a":
        print(input_string[:letters+1])
        print(input_string[letters+1:])
#eg Buffalo, binance


def SortArray(arr):
    output_array = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pass
        if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

                x = arr[i] ** 2
                output_array.append(x)
        else:
                x = arr[i] ** 2
                output_array.append(x)

    return output_array

print(SortArray([3,2,1]))