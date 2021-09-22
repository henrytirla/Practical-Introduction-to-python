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

alpha ='abcdefghijklmnopqrstuvwxyz'
for i in range(1,len(alpha),1):
   print(alpha[i:]+alpha[:i], sep='')
