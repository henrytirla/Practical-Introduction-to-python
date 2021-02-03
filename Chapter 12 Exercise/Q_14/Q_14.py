"""Write a simple spell-checking program. The user should enter a string and the program
should print out a list of all the words it thinks are misspelled. These would be all the words
it cannot find in a wordlist."""

file1 = open("wordlist.txt","r")
str_data = [line.strip("\n") for line in file1]

count =0
user_input = input("Enter a Word : ")
for words in str_data:
  if user_input[:4] == words[:4] :
      if user_input not in words:
          print(words)
