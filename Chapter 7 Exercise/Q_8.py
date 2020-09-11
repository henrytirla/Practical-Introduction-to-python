# Write a program that asks the user for an integer and creates a list that consists of the factors
# of that integer.


input_int=eval(input("Enter Interger: "))
number_list=[]


for i in range(1,input_int+1):
    if input_int%i == 0:
        number_list.append(i)

print(number_list)
