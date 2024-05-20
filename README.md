
# CricinfoAPI

A useful Python wrapper to scrape the ESPN Cricinfo JSON API.



## Installation
```bash
# Development Version

pip install git+https://github.com/UnrealFar/cricinfoapi
```

# Example Usage

Check `examples.py` for more examples of how to use the library.

For getting series/league details, get series ID from the series' Cricinfo URL.
Some examples are given in `cricinfo.SERIES_IDS`

```py
>>> from cricinfo import Series
>>> ipl = cricinfo.SERIES_IDS["IPL"]
>>> ipl.name
Indian Premier League
```

For getting player info, get the player ID from the player's Cricinfo URL.

```py
>>> from cricinfo import Athlete
>>> kohli = Athlete(id=253802)
>>> kohli.name
'Virat Kohli'
```
