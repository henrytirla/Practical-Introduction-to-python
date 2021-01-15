"""You are given a file namelist.txt that contains a bunch of names. Some of the names are
a first name and a last name separated by spaces, like George Washington, while others have
a middle name, like John Quincy Adams. There are no names consisting of just one word or
more than three words. Write a program that asks the user to enter initials, like GW or JQA,
and prints all the names that match those initials. Note that initials like JA should match both
John Adams and John Quincy Adams."""

with open("namelist.txt") as n:
    s = n.readlines()
lines =[line.strip() for line in s]
str_data = [line.split(" ") for line in lines]
Init =(input("Enter User Initial: "))
initial= list(Init) ##Most crucial part for me

for list in str_data:
    if len(initial) >=2:
       if initial[0] == list[0][:1] or initial[1] == list[1][:1]:
           print(list)
    else:
        print("Enter Two Initials Atleast")
        break












