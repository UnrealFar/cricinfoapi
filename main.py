
from cricinfo import Series, SERIES_IDS

# Get the IPL series and season(2024 is latest)
ipl = Series(SERIES_IDS['IPL'])

season = ipl.season

print(ipl.name, season.year)

# Print the names of the teams in the season
teams = season.teams

print("Teams:", [team.name for team in teams])

# Get a team and print its athletes(players)
rcb = season.get_team("rcb") # this can be full name or abbreviation of team
print("Team:", rcb.name)

athletes = rcb.athletes

print("Athletes of RCB:", [athlete.name for athlete in athletes])

# Lets select a particular player
kohli = rcb.get_athlete("kohli") # this can be full name or abbreviation of player

print("Player:", kohli.name)
print("Birthdate:", kohli.date_of_birth)
