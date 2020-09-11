# Start with the list [8,9,10]. Do the following:
# (a) Set the second entry (index 1) to 17
# (b) Add 4, 5, and 6 to the end of the list
# (c) Remove the first entry from the list
# (d) Sort the list
# (e) Double the list
# (f) Insert 25 at index 3
# The final list should equal [4,5,6,25,10,17,4,5,6,10,17]

number_list =[8,9,10]

number_list[1]=17
number_list.append(4)
number_list.append(5)
number_list.append(6)
number_list.pop(0)
number_list.sort()

ls =[]
for i in number_list:
    ls.append(i)

number_list.extend(ls)

number_list.insert(3,25)


print(number_list)

