# Write a program that rotates the elements of a list so that the element at the first index moves
# to the second index, the element in the second index moves to the third index, etc., and the
# element in the last index moves to the first index.

num = [1,2,3,4,5]
reverse_list = []

for i in range( len(num)):
   reverse_list.append(num[i-1])

print("Normal List",num,"Reversed list", reverse_list)


