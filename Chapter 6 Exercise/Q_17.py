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
list_alphabet = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
j=0
for i in range(len(list_alphabet)):
    print("---",list_alphabet[i], end="")
    for j in range(i + 1, len(list_alphabet)):
        print(list_alphabet[j],end="")

##Not complete solution
