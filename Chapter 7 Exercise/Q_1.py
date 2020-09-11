# Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the
# result.

count =0
count_num =0
# number_list =eval(input('Enter numberlist: '))
number_list =[1,24,3,2,4,5]
print("Total number of items in list",len(number_list))
print("Last item in list" ,number_list[-1])
print("Reverse List",number_list[::-1])

for i in range(len(number_list)):
   if number_list[i] == 5:
      count +=1
print("YES FOUND FIVE", count)

number_list.pop(0)
number_list.pop(-1)
number_list.sort()
print("After pop and sort",number_list)

for i in range(len(number_list)):
    if number_list[i] < 5:
       count_num += 1
print("Numbers of digits less than 5 ", count_num)




