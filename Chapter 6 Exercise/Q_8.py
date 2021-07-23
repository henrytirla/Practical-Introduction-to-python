"""At a certain school, student email addresses end with @student.college.edu, while professor
email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then has the user enter those addresses.
After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some professor
addresses entered."""


num_of_email = int(input("Enter the number of emails: "))
n = 0
student_count = 0
teacher_count = 0

while n < num_of_email:
    email = input("Enter Student or `Teacher Email: ")
    if "prof" in email:
        teacher_count += 1
        n +=1
    elif "student" in email:
        student_count += 1
        n +=1


if teacher_count == num_of_email:
    print("All emails were that of teachers")
if student_count == num_of_email:
        print("All emails were that of student")
if  student_count != num_of_email and teacher_count != 0:
       print("Email list contained both professors and student email")


