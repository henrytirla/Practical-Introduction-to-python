# Ask the user to enter a list of strings. Create a new list that consists of those strings with their
# first characters removed.


input_string = input("Enter String for list: ").split(",")
string_list = []
string_list.extend(input_string)
print(string_list)


for i in range(len(string_list)):
    string_list[i]=string_list[i][1:]

print(string_list)