"""Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'."""

user_input =input("Enter Text: ") #love is a beautiful and profound an angelic being
articles =["a","an","and"]
words =user_input.split()
count =0

for word in words:
    if word in articles:
        count +=1
print(count)
