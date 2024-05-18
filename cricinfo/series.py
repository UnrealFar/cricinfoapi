from __future__ import annotations

from typing import List, TYPE_CHECKING

from .base import BaseModel
from .season import Season


SERIES_IDS = {
    'BBL': 8044,
    'IPL': 8048,
    'Ranji Trophy': 8050,
    'T20 World Cup': 8038,
    'World Cup': 8039,
}
"""Series IDs for some popular cricket leagues.
You can find more series IDs by visiting the ESPN Cricinfo website.
"""

class Series(BaseModel):
    """A cricket series."""

    if TYPE_CHECKING:
        id: int
        group_id: int
        name: str
        alt_name: str
        short_name: str
        short_alt_name: str
        abbreviation: str
        slug: str
        is_tournament: bool
        season_url: str
        seasons_url: str
        teams_url: str
        events_url: str
        notes_url: str
        groups_url: str
        rankings_url: str



    def __init__(self, id: int):
        self.id = id
        self.json_url = f"http://core.espnuk.org/v2/sports/cricket/leagues/{self.id}/"
        self.json = j = self.get_json(self.json_url)

        self.group_id = j['groupId']
        self.name = j['name']
        self.alt_name = j['alternateName']
        self.short_name = j['shortName']
        self.short_alt_name = j['shortAlternateName']
        self.abbreviation = j['abbreviation']
        self.slug = j['slug']
        self.is_tournament = j['isTournament']

        self.season_url = j['season']["$ref"]
        self.seasons_url = j['seasons']["$ref"]
        self.teams_url = j['teams']["$ref"]
        self.events_url = j['events']["$ref"]
        self.notes_url = j['notes']["$ref"]
        self.groups_url = j['groups']["$ref"]
        self.rankings_url = j['rankings']["$ref"] # no clue why but rankings don't work

        self._season = None
        self._seasons = None

    @property
    def season(self) -> Season[Series, str]:
        """Returns the current season of the series."""
        if self._season is None:
            self._season = Season(self, self.season_url)
        return self._season

    @property
    def seasons(self) -> List[Season[Series, str]]:
        """Returns a list of seasons in the series."""
        if self._seasons is None:
            self._seasons = []
            j = self.get_json(self.seasons_url)
            for s in j['items']:
                self._seasons.append(Season(self, s['$ref']))
        return self.get_json(self.seasons_url)['items']

    @property
    def years(self) -> List[str]:
        """Returns a list of years in the series."""
        return [s.year for s in self.seasons]

class League(Series):
    """Alternative name for Series."""
    ...
