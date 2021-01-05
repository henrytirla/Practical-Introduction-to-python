"""
You are given a file called grades.txt, where each line of the file contains a one-word student
username and three test scores separated by spaces, like below:.
GWashington 83 77 54
JAdams 86 69 90
Write code that scans through the file and determines how many students passed all three
tests.
"""

passed_all3 =[]
failed_atleast1 =[]
with open("grades.txt") as f:
    s = f.readlines()
    lines = [line.strip() for line in s]
    structure_content = [line.split(" ") for line in lines ]

    for score in structure_content:
        c = 0
        for i in range(1, len(score)):

            if int(score[i]) > 50 :
               c +=1
            if c == 3:
                passed_all3.append(score[0])
        if c !=3:
           failed_atleast1.append(score[0])    


print("Student who passed all three Subjects:",passed_all3,"Their number is",len(passed_all3))
print("Student who Failed Atleast 1 Subject:",failed_atleast1,"Their number is",len(failed_atleast1))
           








