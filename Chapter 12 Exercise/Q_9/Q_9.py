"""
Benford’s law states that in real data where the values are spread across several orders of
magnitude, about 30% of the values will start with the number 1, whereas only about 4.6%
of the values will start with the number 9. This is contrary to what we might expect, namely
that values starting with 1 and 9 would be equally likely. Using the file expenses.txt which
consists of a number of costs from an expense account, determine what percentage start with
each of the digits 1 through 9. This technique is used by accountants to detect fraud.
"""


file1 = open("expenses.txt","r")
str_data =[line.strip("\n") for line in file1]

total = len(str_data)
percentage_occurence =[]


count = 0
for benford_law in range(1,10):

    for number in range(0,len(str_data)):
        value = str_data[number][:1]
        if int(str_data[number][:1]) == benford_law:
            count = count + 1
    percentage = count/total * 100
    percentage_occurence.append([benford_law,"Occurence Percentage is ",percentage])
    count = 0


print(percentage_occurence)
