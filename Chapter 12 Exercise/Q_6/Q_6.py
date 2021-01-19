"""You are given a file namelist.txt that contains a bunch of names. Print out all the names in the list in which the vowels a, e, i, o, and u appear in order (with repeats possible). The first vowel in the name must be a and after the first u, it is okay for there to be other vowels. An example is Ace Elvin Coulson."""

#structure each word
#put each word to be tried against aeiou

with open("namelist.txt") as n:
    s = n.readlines()
lines= [line.strip for line in s ]
str_data = [line.split(" ") for line in lines]
vowel =['a','e','i','o','u']

print(str_data)





