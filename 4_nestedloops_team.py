#NESTED LOOPS WHERE THE FIRST CHOICE MATTERS:
#Eg :-pairing teams for home and away games

print("this script creates a combination of two teams and checks that it is not playing agianst itself")
teams =["mickey", "Donald", "Daisy", "Goofy"]
for home_teams in teams:
    for away_teams in teams:
        if home_teams != away_teams:
            print(home_teams + " vs " + away_teams)
