from __future__ import annotations

from typing import List, overload
from datetime import datetime

from .base import BaseModel

from .athlete import Athlete



class Team[Q: str | int | None](BaseModel):

    @overload
    def __init__(
        self,
        *,
        league_id: int,
        id: int,
    ):
        pass

    @overload
    def __init__(
        self,
        *,
        team_url: str,
    ):
        pass

    def __init__(
        self,
        *,
        team_url: Q = None,
        league_id: Q = None,
        id: Q = None,
    ):
        if id and league_id:
            self.json_url = f"http://core.espnuk.org/v2/sports/cricket/leagues/{league_id}/teams/{id}/"
        else:
            self.json_url = team_url
        self.json = j = self.get_json(self.json_url)

        self.id = j['id']
        self.name = j['name']
        self.nickname = j['nickname']
        self.abbreviation = j['abbreviation']
        self.display_name = j['displayName']
        self.short_display_name = j['shortDisplayName']
        self.is_national = j['isNational']
        self.is_active = j['isActive']
        self.country_code = j['countryCode']
        self.slug = j['slug']

        self.athletes_url = j['athletes']["$ref"]
        self._athletes = []

    def __repr__(self) -> str:
        return f"<Team {self.name}>"

    @property
    def athletes(self) -> List[Athlete[str]]:
        """Returns a list of athletes in the team."""
        if not self._athletes:
            j = self.get_json(self.athletes_url)
            for a in j['items']:
                self._athletes.append(Athlete(player_url=a['$ref']))
        return self._athletes
