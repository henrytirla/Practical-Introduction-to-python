"""(a) Write a program that uses a while loop (not a for loop)
to read through a string and print
the characters of the string one-by-one on separate lines.
(b) Modify the program above to print out every second character of the string"""

s = "Sorry"
num =0
while num < len(s):
    print(s[num])
    #num += 1   ## a()
    num += 2 ## b