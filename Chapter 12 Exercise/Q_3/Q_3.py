"""
You are given a file called logfile.txt that lists log-on and log-off times for users of a
system. A typical line of the file looks like this:
Van Rossum, 14:22, 14:37

Each line has three entries separated by commas: a username, a log-on time, and a log-off
time. Times are given in 24-hour format. You may assume that all log-ons and log-offs occur
within a single workday.
Write a program that scans through the file and prints out all users who were online for at
least an hour.
"""
file = open("logfile.txt")
lines = [line.strip() for line in file ]
structure_data = [line.split(" ") for line in lines]

for line in structure_data:
    for time in range(1,len(line)):
        log_of = ((int(line[2][:2])) + (int(line[2][-2:])) / 60)
        log_in = ((int(line[1][:2])) + (int(line[1][3:-1])) / 60)
        time_onine = log_of - log_in
        #print(log_of)
        #print("log in",log_in)
        if time_onine >= 1:
            print(line[0]," Have Been Active For Over An Hour.",time_onine)





