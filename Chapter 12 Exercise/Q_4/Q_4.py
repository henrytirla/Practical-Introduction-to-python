"""
You are given a file called students.txt. A typical line in the file looks like:
walter melon melon@email.msmary.edu 555-3141
There is a name, an email address, and a phone number, each separated by tabs. Write a
program that reads through the file line-by-line, and for each line, capitalizes the first letter
of the first and last name and adds the area code 301 to the phone number. Your program
should write this to a new file called students2.txt. Here is what the first line of the new
file should look like:
Walter Melon melon@email.msmary.edu 301-555-3141
"""


with open("student.txt") as student:
    s =student.readlines()

lines= [line.strip() for line in s]
#print(lines)
structure_content = [line.split(" ") for line in lines]
print("structured Content",structure_content)

for data in structure_content:

    data[0] = data[0].title()
    data[1] = data[1].title()
    data[3] = "305-" + data[3]
f= open("student2.txt","w")
for lines in structure_content:
    print(lines,file=f)
#print(structure_content)








