
from cricinfo import Series, SERIES_IDS

# Get the IPL series and season(2024 is latest)
series = Series(SERIES_IDS['IPL'])

season = series.season

print(series.name, season.year)

# Print the names of the teams in the season
teams = season.teams

print(team.name for team in teams)



