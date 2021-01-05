"""
You are given a file called class_scores.txt, where each line of the file contains a oneword
username and a test score separated by spaces, like below:.
GWashington 83
JAdams 86
Write code that scans through the file, adds 5 points to each test score, and outputs the usernames
and new test scores to a new file, scores2.txt.


"""

lines = [line.strip() for line in open("class_scores.txt")]
inside_lines = [line.split(' ') for line in lines]
print("inside lines",inside_lines)
for num in inside_lines:
    num[1]=str(int(num[1])+5)

lines=[" ".join(line) for line in inside_lines]
print("Lines",lines)


f=open('scores2.txt','w')

for line in lines:
    print(line,file=f)






