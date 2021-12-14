"""

Write a program that asks the user to enter a sentence and
 then randomly rearranges the words of the sentence.
 Don’t worry about getting punctuation or capitalization correct.

 b) Do the above problem, but now make sure that the sentence starts with a capital, that
the original first word is not capitalized if it comes in the middle of the sentence, and
that the period is in the right place.
"""

from random import shuffle
from string import punctuation
#user_sentence = input("Enter a sentence:  ")
user_sentence = "I am a crypto billionaire ."
#eg I am a crypto billionaire .
#a
L =user_sentence.split()
shuffle(L)

print(L)


#b

punct =""
sentence2=""
if user_sentence[-1] in punctuation:
    punct = user_sentence[-1]
    sentence2 = user_sentence[0].lower() + user_sentence[1:-1]



#print(sentence2)
l2= sentence2.split()

shuffle(l2)
sentence2 = ' '.join(l2) + punct
sentence2 = sentence2[0].upper() + sentence2[1:]
print(sentence2)

#b credit to https://github.com/Yaachaka/  for the solution of b