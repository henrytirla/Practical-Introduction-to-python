"""You are given a file called baseball.txt. A typical line of the file starts like below.
Ichiro Suzuki SEA 162 680 74 ...[more stats]

Each entry is separated by a tab, \t. The first entry is the player’s name and the second is
their team. Following that are 16 statistics. Home runs are the seventh stat and stolen bases
are the eleventh. Print out all the players who have at least 20 home runs and at least 20 stolen
bases."""

file1 = open("baseball.txt","r")
#print(file1.read())
str_data =[lines.split() for lines in file1]

for player in str_data:
    if len(player) > 13:
        if int(player[9]) > 20 and int(player[13] )>= 20:
           print("Player Names: ", player[0:2])