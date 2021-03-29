"""Write a program that allows the user to enter any number of test scores. The user indicates
they are done by entering in a negative number. Print how many of the scores are A’s (90 or
above). Also print out the average."""
scores=[]
count=0
while True:
    testscore =eval(input("Enter Test Cores: "))
    scores.append(testscore)
    if testscore >= 90:
        count+=1

    if testscore == 0:
        print("Count Agrade",count)
        print("Average",sum(scores)/len(scores))