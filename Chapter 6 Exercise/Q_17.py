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

alphabet="abcdefghijklmnopqrstuvwxyz"

for m in range (26):
    for j in range (26):
        print(alphabet[(m+j)%26],end='')
    print()

