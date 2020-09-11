"""Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space
"""

enter_string = input("Enter Your Full names: ")

print("(a)" , len(enter_string))
print("(b)", enter_string * 10)
print("(c)", enter_string[:1])
print("(d)",enter_string[:3])
print("(e)", enter_string[-3:])
print("(f)",enter_string[::-1])

if len(enter_string) > 7:
    print("(g)",enter_string[:7])
else:
    print("(g)","String not long enough")

print("(h)", enter_string[1:-1])

print("(i)",enter_string.upper())
for  a in  range(len(enter_string)):
    if enter_string[a] == 'a':
        enter_string = enter_string.replace('a', "e")
        print("(j)",enter_string)




for  a in  range(len(enter_string)):
    if enter_string.isalpha():
        enter_string = enter_string.replace(enter_string, " ")
        print("(k)",enter_string,end="")




