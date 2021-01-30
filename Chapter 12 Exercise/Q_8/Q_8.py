"""
For this problem, use the file of NCAA basketball scores as described in Section 12.3.
(a) Find the average of the points scored over all the games in the file.
(b) Pick your favorite team and scan through the file to determine how many games they
won and how many games they lost.
(c) Find the team(s) that lost by 30 or more points the most times
(d) Find all the teams that averaged at least 70 points a game.
(e) Find all the teams that had winning records but were collectively outscored by their
opponents. A team is collectively outscored by their opponents if the total number of
points the team scored over all their games is less than the total number of points their
opponents scored in their games against the team.
"""

file1 = open("scores.txt","r")
str_data = [line.split() for line in file1]


#print(str_data)
#a)
scorelist=[]
for scores in str_data:
    scorelist.extend([scores[2],scores[4]])
for i in range(0,len(scorelist)):  ##convert string to INT
    scorelist[i] = int(scorelist[i])



average = sum(scorelist)/len(scorelist)
#print("Average",average)

#b)

myteam ="AlcornSt."
team1=[]
team2 =[]
for teams   in str_data:
    if teams[1] == myteam:
       team1.append(teams[1:])
    if teams[3] == myteam:
       team2.append(teams[1:])

wins= 0
loss =0
for matches in team1:
    if int(matches[1]) > int(matches[3]):
        wins = wins + 1
        print("wins")
    else:
        loss = loss +1

for matches in team2:
    if int(matches[3]) > int(matches[1]):
        wins = wins + 1

    else:
        loss = loss +1
#print(myteam,"Won: ", wins,"Matches and Lost: ",loss,"Matches")

#c)
looser_team =[]
for teams   in str_data:
    if int(teams[2]) - int(teams[4]) >= 30:
        if teams[3] not in looser_team:
             looser_team.append(teams[3])

    if int(teams[4]) - int(teams[2]) >= 30:
        if teams[1] not in looser_team:
             looser_team.append(teams[1])

#print("Teams who lost Match with Atleast 30 or more points",looser_team)


#d)
winner_teams=[]
for teams   in str_data:
    if int(teams[4]) - int(teams[2]) >= 70:
        #if teams[3] not in looser_team:
           winner_teams.append(teams[3])
#print(winner_teams)



#e