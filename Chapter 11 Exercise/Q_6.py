"""Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2. Store
this information in a dictionary where the keys are the team names and the values are lists of
the form [wins, losses]."""



def teamInfo():
   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(teamInfo())