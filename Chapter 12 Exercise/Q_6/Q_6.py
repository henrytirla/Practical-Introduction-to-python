"""You are given a file namelist.txt that contains a bunch of names.
Print out all the names in the
list in which the vowels a, e, i, o, and u appear in order
(with repeats possible).
The first vowel in the name must be a and after the first u,
it is okay for there to be other vowels. An example is Ace Elvin Coulson."""

#structure each word
#put each word to be tried against aeiou

vowel =['A','E','I','O','U']
with open("namelist.txt") as n:
    s = n.readlines()
lines= [line.strip() for line in s ]
str_data =[line.split(' ') for line in lines]



for names in str_data:
    for i in range(len(names)):
       if names[i][:1] == vowel[0]  and names[i+1][:1] ==vowel[1] and names[i+2][:1] == vowel[2] and names[i+3][:1] == vowel[3]  and names[i+4 ][:1] == vowel[4]   :
                print(names)




