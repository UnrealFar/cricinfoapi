
# Output at bottom file

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


OUTPUT = """
Indian Premier League 2024
Teams: ['Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Punjab Kings', 'Rajasthan Royals', 'Royal Challengers Bengaluru', 'Sunrisers Hyderabad']
Team: Royal Challengers Bengaluru
Athletes of RCB: ['Faf du Plessis', 'Akash Deep', 'Anuj Rawat', 'Manoj Bhandage', 'Saurav Chauhan', 'Tom Curran', 'Mayank Dagar', 'Lockie Ferguson', 'Cameron Green', 'Will Jacks', 'Alzarri Joseph', 'Dinesh Karthik', 'Virat Kohli', 'Mahipal Lomror', 'Glenn Maxwell', 'Mohammed Siraj', 'Rajat Patidar', 'Suyash Prabhudessai', 'Rajan Kumar', 'Himanshu Sharma', 'Karn Sharma', 'Swapnil Singh', 'Reece Topley', 'Vijaykumar Vyshak', 'Yash Dayal']
Player: Virat Kohli
Birthdate: 1988-11-05 00:00:00
"""

