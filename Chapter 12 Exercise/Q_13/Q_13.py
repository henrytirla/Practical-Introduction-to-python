"""Print out all combinations of the string 'Python' plus a three letter English word. Capitalize
the first letter of the three letter word. Example combinations are 'PythonCat',
'PythonDog', and 'PythonTag'. These are valid combinations because cat, dog, and tag
are English words. On the other hand, 'PythonQqz' would not be a valid combination because
qqz is not an English word. Use a wordlist to determine which three letter combinations
are words."""

file1 = open("wordlist.txt","r")
str_data = [line.strip("\n") for line in file1]
str = "Python"
for words in str_data:
    if len(words) ==3:
        c=words.title()
        print(str + c)
        