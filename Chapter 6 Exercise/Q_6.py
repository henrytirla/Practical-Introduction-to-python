
"""Write a program that asks the user to enter a string s and then converts s to lowercase, removes
all the periods and commas from s, and prints the resulting string."""


input_string= input("Please Enter a String: ")
input_string = input_string.lower()
input_string = input_string.replace('.','')
input_string = input_string.replace(',','')
print(input_string)

# Example This , is a beautiful , day.
