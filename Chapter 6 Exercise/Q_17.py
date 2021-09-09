"""
Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy
"""
list_alphabet = ["a", "b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in  range(len(list_alphabet)):
    print(list_alphabet[i],end="")