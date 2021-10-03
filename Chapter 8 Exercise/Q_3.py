"""(a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence."""

user_input = input("Enter a sentence: ")
#eg I love you ethan tirla and I promise to give you the best life has to offer
sentence_words = user_input.split()

print("a",sentence_words[2])

for word in range(2,len(sentence_words),3):
    print("b",sentence_words[word])
