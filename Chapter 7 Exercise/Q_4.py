# Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
# entries in the list that are greater than 10 with 10.

input_num = eval(input("Enter List of Nmber: "))
number_list =[]
number_list.extend(input_num)
print(number_list)
for i in range(len(number_list)):
    if number_list[i] > 10:
        number_list[i] = 10


print(number_list)