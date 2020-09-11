"""Write a program that asks the user to enter a word and prints out whether that word contains
any vowels."""
# print(vowels[j], j)
vowels =['a','e','i','o','u']
count =0
word =input("Enter Word: ")
for i in range(len(word)):
    for j in range(5):
        if vowels[j] in word[i]:
            count += 1



print(count)








