"""Repeatedly ask the user to enter a team name and the how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins, losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out
the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records."""


def teamWIn():
    numberofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(numberofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)




        #return("a",team_name,percentage_win,"%")
    #return " a) Team {} Has a wining  of {}ff{} %".format(team_name,percentage_win,team_dict)
        # for team_winning_score in team_dict.values():
        #     scorelist=[]
        #     scorelist.append(value)
        # return "Score list is {}".format(scorelist)


print(teamWIn())